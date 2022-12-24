import json

from db_handler.mysql_dbconn import DbConnection
from db_handler.db_vars import (
    ENDPOINT_URL,
    USERNAME,
    PASSWORD,
    DB_NAME
)
from common_handlers import (
    validate_question,
    validate_user,
    validate_commment
)

def respond_discussion(event, context):
    """Respond Discussion Lambda function
    This Lambda Funcion will respond a discussion and save it in DataBase

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        started_by: string, required
            Name of the user starting the Discussion Question
        
        question: string, required
            Question to be put in the Discussion Question

        comment: string, required
            Comment to be linked with the Discussion Question

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

            comment_id: int, if successful response
                ID number for the recently created response (comment)
    """

    out = {
            "statusCode": 500,
            "body": {
                "message": "Internal server error"
            }
        }
    
    try:
        event = json.loads(event.get("body"))
        question = event.get('question')
        started_by = validate_user(event.get('started_by'))
        comment = event.get(('comment'))

        if validate_question(question) == False:
            out["statusCode"] = 400
            out["body"]["message"] = "Invalid question. Questions must have text"
            out["body"] = json.dumps(out["body"])
            return out

        if validate_commment(comment) == False:
            out["statusCode"] = 400
            out["body"]["message"] = "Invalid comment. Comment must have text"
            out["body"] = json.dumps(out["body"])
            return out


        my_db = DbConnection(host=ENDPOINT_URL, user=USERNAME, passwd=PASSWORD, db_name=DB_NAME)
        out_discussion_question_params = my_db.call_sp_with_out("sp_Read_Discussion_Question", "all", *[question, 0])

        # Validate that discussion exists
        if out_discussion_question_params[0] == 0:
            out["statusCode"] = 400
            out["body"]["message"] = "Invalid question. Cannot respond an unexistent discussion"
            out["body"] = json.dumps(out["body"])
            return out

        out_comment_params = my_db.call_sp_with_out("sp_Create_Comment", "all", *[started_by, comment, 0])

        if out_comment_params and out_comment_params[0] > 0:
            # Link the comment to discussion
            my_db.call_sp_with_out("sp_Create_Rel_Discussion_Question_Response", "all", *[question, out_comment_params[0]])
            
            out["statusCode"] = 201
            out["body"]["message"] = "Created new response"
            out["body"]["comment_id"] = out_comment_params[0]
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
