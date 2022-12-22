import json

from discussion.db_handler.mysql_dbconn import DbConnection
from discussion.db_handler.db_vars import (
    ENDPOINT_URL,
    PORT,
    USERNAME,
    PASSWORD,
    DB_NAME
)

def start_discussion(event, context):
    """Create Discussion Question Lambda Function

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
        started_by = event['started_by']
        question = event['question']

        if len(started_by) == 0:
            started_by = 'Anon'

        if len(question) == 0:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "Bad Request, invalid question"
                }),
            }

        my_db = DbConnection(host=ENDPOINT_URL, user=USERNAME, passwd=PASSWORD, db_name=DB_NAME)
        out_parameters = my_db.call_sp_with_out("sp_Create_Discussion_Question", "all", *[started_by, question, 0])
        result = "Created New Discussion"
        status_code = 201
    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)
        result = "Failed"
        status_code = 500
        out_parameters = [0]
        raise e

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": result,
            "Discussion ID": out_parameters[0]
        }),
    }
