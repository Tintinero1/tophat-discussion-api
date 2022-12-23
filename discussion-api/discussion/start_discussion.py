import json

from discussion.db_handler.mysql_dbconn import DbConnection
from discussion.db_handler.db_vars import (
    ENDPOINT_URL,
    USERNAME,
    PASSWORD,
    DB_NAME
)
from discussion.common import (
    validate_user,
    validate_question
)

def start_discussion(event, context):
    """Create Discussion Question Lambda Function
    This Lambda Funcion will start a discussion and save it in DataBase

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        started_by: string, required
            Name of the user starting the Discussion Question
        
        question: string, required
            Question to be put in the Discussion Question

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

            discussion_id: int, if successful response
                ID number for the recently created discussion if applies
    """

    try:
        started_by = validate_user(event['started_by'])
        question = event['question']
        out = {
            "statusCode": 500,
            "body": {
                "message": "Internal server error"
            }
        }

        if validate_question(question) == False:
            out["statusCode"] = 400
            out["body"]["message"] = "Invalid question. Questions must have text"
            out["body"] = json.dumps(out["body"])
            return out

        my_db = DbConnection(host=ENDPOINT_URL, user=USERNAME, passwd=PASSWORD, db_name=DB_NAME)

        out_discussion_parameters = my_db.call_sp_with_out("sp_Create_Discussion_Question", "all", *[started_by, question, 0])

        if out_discussion_parameters and out_discussion_parameters[0] > 0:
            out["statusCode"] = 201
            out["body"]["message"] = "Created new discussion"
            out["body"]["discussion_id"] = out_discussion_parameters[0]
            out["body"] = json.dumps(out["body"])

    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)
        out["statusCode"] = 500
        out["body"]["message"] = "Internal server error"
        out["body"] = json.dumps(out["body"])
        raise e

    return out
