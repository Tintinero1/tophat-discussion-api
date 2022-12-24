import json

from db_handler.mysql_dbconn import DbConnection
from db_handler.db_vars import (
    ENDPOINT_URL,
    USERNAME,
    PASSWORD,
    DB_NAME
)
from common_handlers import (
    validate_question
)

def get_all_comments(event, context):
    """Get All Comments Lambda function
    This Lambda Funcion will retrieve all comments available in the DataBase in a flat tree for a given discussion

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        question: string, required
            Discussion Question where the comments will be retrieved from

    context: object, required
        Lambda Context runtime methods and attributes

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        statusCode: int
            HTTP Status Code
        
        body: dict

            message: string
                Message response from the backend

            comments: list, if successful response
                List of all comments available in the DataBase in a flat tree 
    """

    out = {
            "statusCode": 500,
            "body": {
                "message": "Internal server error"
            }
        }

    try:
        event = event.get("queryStringParameters")
        question = event.get("question")

        if validate_question(question) == False:
            out["statusCode"] = 400
            out["body"]["message"] = "Invalid question. Questions must have text"
            out["body"] = json.dumps(out["body"])
            return out

        my_db = DbConnection(host=ENDPOINT_URL, user=USERNAME, passwd=PASSWORD, db_name=DB_NAME)
        out_discussion_question_params = my_db.call_sp_with_out("sp_Read_Discussion_Question", "all", *[question, 0])

        # Validate that discussion exists
        if out_discussion_question_params[0] == 0:
            out["statusCode"] = 400
            out["body"]["message"] = "Invalid question. Question does not exists"
            out["body"] = json.dumps(out["body"])
            return out
        
        # Build root node discussion question and append it
        result = []
        discussion_question = my_db.call_sp("sp_Read_Discussion", "all", *[question])[0]
        discussion_question_info = {
            "id": 1,
            "id_discussion_question": discussion_question[0],
            "started_by": discussion_question[1],
            "Question": discussion_question[2],
            "parent_id": 0
        }
        result.append(discussion_question_info)

        # Gets all first level comments
        comments = my_db.call_sp("sp_Read_Discussion_Response", "all", *[question])

        if len(comments) == 0:
            out["statusCode"] = 404
            out["body"]["message"] = "No commments available for this discussion"
            out["body"] = json.dumps(out["body"])
            return out

        # Traverse all first level comments
        for x in comments:
            comment_info = {
                "id": x[0]+1,
                "comment_id": x[0],
                "started_by": x[1],
                "comment": x[2],
                "parent_id": 1
            }
            def flatten_tree(comment, result:list):
                result.append(comment)
            
                # Get all replies for a comment
                responses = my_db.call_sp("sp_Read_Responses", "all", *[comment["comment_id"]])
                
                # Add replies in recursion
                for response in responses:
                    response_info = {
                        "id": response[0]+1,
                        "comment_id": response[0],
                        "started_by": response[1],
                        "comment": response[2],
                        "parent_id": comment["id"]
                    }
                    flatten_tree(response_info, result)

            flatten_tree(comment_info, result)
            
        if len(result) > 0:
            out["statusCode"] = 200
            out["body"]["message"] = "All messages retrieved"
            out["body"]["comments"] = result
            out["body"] = json.dumps(out["body"])
            return out
            
        out["body"] = json.dumps(out["body"])
    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)
        out["statusCode"] = 500
        out["body"]["message"] = "Internal server error"
        out["body"] = json.dumps(out["body"])
        raise e

    return out
