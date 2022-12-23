import json

from discussion.respond_discussion import respond_discussion
from discussion.db_handler.mysql_dbconn import DbConnection
from discussion.db_handler.db_vars import (
    ENDPOINT_URL,
    USERNAME,
    PASSWORD,
    DB_NAME
)
from discussion.common import (
    validate_comment_id,
    validate_commment,
    validate_user
)

def respond_comment(event, context):
    """Create Respond Lambda function
    This Lambda Funcion will start a discussion and save it in DataBase

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        comment_id: int, required
            ID of the comment to be responded

        started_by: string, required
            Name of the user that will be responding the comment
        
        response: string, required
            Response (comment) to be linked with the comment_id

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

    try:
        comment_id = event['comment_id']
        started_by = validate_user(event['started_by'])
        response = event['response']
        out = {
            "statusCode": 500,
            "body": {
                "message": "Internal server error"
            }
        }

        if validate_comment_id(comment_id) == False:
            out["statusCode"] = 400
            out["body"]["message"] = "Invalid comment id. comment id must be a number"
            out["body"] = json.dumps(out["body"])
            return out

        if validate_commment(response) == False:
            out["statusCode"] = 400
            out["body"]["message"] = "Invalid response. Response must have text"
            out["body"] = json.dumps(out["body"])
            return out

        # Create the response in the DB and retrieve the comment id
        my_db = DbConnection(host=ENDPOINT_URL, user=USERNAME, passwd=PASSWORD, db_name=DB_NAME)
        out_comment_params = my_db.call_sp_with_out("sp_Create_Comment", "all", *[started_by, response, 0])

        if out_comment_params and out_comment_params[0] > 0:
            # Link the response to the comment
            response_id = out_comment_params[0]
            my_db.call_sp_with_out("sp_Create_Rel_Comment_Response", "all", *[comment_id, response_id])

            out["statusCode"] = 201
            out["body"]["message"] = "Created new response"
            out["body"]["comment_id"] = out_comment_params[0]
            out["body"] = json.dumps(out["body"])

    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)
        out["statusCode"] = 500
        out["body"]["message"] = "Internal server error"
        out["body"] = json.dumps(out["body"])
        raise e

    return out
