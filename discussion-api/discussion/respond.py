import json

from discussion.respond_discussion import respond_discussion
from discussion.db_handler.mysql_dbconn import DbConnection
from discussion.db_handler.db_vars import (
    ENDPOINT_URL,
    PORT,
    USERNAME,
    PASSWORD,
    DB_NAME
)

def respond(event, context):
    """Respond Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:
        comment_id = event['comment_id']
        started_by = event['started_by']
        response = event['response']

        # Create the response in the DB and retrieve the comment id
        my_db = DbConnection(host=ENDPOINT_URL, user=USERNAME, passwd=PASSWORD, db_name=DB_NAME)
        out_comment_params = my_db.call_sp_with_out("sp_Create_Comment", "all", *[started_by, response, 0])
        response_id = out_comment_params[0]

        # Link the response to the comment
        my_db.call_sp_with_out("sp_Create_Rel_Comment_Response", "all", *[comment_id, response_id])

        status_code = 201
        if out_comment_params and out_comment_params[0] > 0:
            message = "Succesfully Responded"
    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)
        status_code = 500
        message = "Error: request not fulfilled"
        
        raise e

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": message,
            "comment_id": out_comment_params[0]
        }),
    }
