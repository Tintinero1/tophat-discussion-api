import json

from discussion.db_handler.mysql_dbconn import DbConnection
from discussion.db_handler.db_vars import (
    ENDPOINT_URL,
    PORT,
    USERNAME,
    PASSWORD,
    DB_NAME
)

def get_all_comments(event, context):
    """Get All Comments Lambda function

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
        question = event["question"]
        my_db = DbConnection(host=ENDPOINT_URL, user=USERNAME, passwd=PASSWORD, db_name=DB_NAME)
        
        # Gets all first level comments
        comments = my_db.call_sp("sp_Read_Discussion_Response", "all", *[question])

        result = []
        # Traverse all first level comments
        for x in comments:
            comment_info = {
                "comment_id": x[0],
                "started_by": x[1],
                "comment": x[2]
            }
            def flatten_tree(comment, result:list):
                result.append(comment)
            
                # Get all replies for a comment
                responses = my_db.call_sp("sp_Read_Responses", "all", *[comment["comment_id"]])
                # print("My response: ", responses)
                
                # Add replies in recursion
                for response in responses:
                    response_info = {
                        "comment_id": response[0],
                        "started_by": response[1],
                        "comment": response[2]
                    }
                    flatten_tree(response_info, result)

            flatten_tree(comment_info, result)
            


        status_code = 201
        message = "All messages retrieved"
        # if out_params[0] > 0:
            

    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)
        message = "Error: request not fulfilled"
        status_code = 500

        raise e

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": message,
            "comments": result,
        }),
    }
