# tophat-discussion-api


# Deploy DataBase

## Creating AWS account and configuring credentials
Create an amazon AWS account [https://signin.aws.amazon.com/]

Create and configure your aws access key credential [https://us-east-1.console.aws.amazon.com/iam/home#/security_credentials$access_key]

In your local terminal type:
    
    `aws configure`

When prompted:
```
    AWS access key ID: paste your AWS access key ID
    AWS Secret Access Key: paste your AWS Secret Access Key
    Default region name: us-west-1
    Default output format: json
```

## SETUP AWS CLI
Please follow instructions from this URL:
```https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html```

## SETUP AWS SAM
Please follow instructions from this URL:
```https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html```

## SETUP MYSQL WORKBENCH
Please install MYSQL Workbench, it will be needed later on:
```https://dev.mysql.com/downloads/workbench/```

## Creating AWS MYSQL DB (AWS RDS)
When in trouble check the official docummentation: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SettingUp.html

**Copy and paste this command in your terminal to create the DB**

```
    aws rds create-db-instance --db-name tophat_discussion_db --engine MySQL \
    --engine-version 8.0.30 \
    --db-instance-identifier "tophatDiscussionDb" --backup-retention-period 3 \
    --db-instance-class db.t3.micro --allocated-storage 5 --publicly-accessible \
    --master-username tophat --master-user-password tophatdiscussionapi
```

```NOTE: Do not save username and password in text documents. This is only for exercise demonstration purposes```

Paste username and password on ```discussion-api/discussion/db_handler/db_vars.py => USERNAME / PASSWORD```

**EDIT security group on AWS console online**

Go to your AWS RDS DB Instances and select tophatdiscussiondb
```https://us-west-1.console.aws.amazon.com/rds/home?region=us-west-1#databases:```

now in the main page on the subpage ```Connectivity & security```
click on your default VPC security group (example: default (sg-047ab15fe2b120f03))

click on your ```Security group ID``` to modify it

click on ```Edit inbound rules```

Delete the only current inbound rule

Click on ```Add rule```

On ```Type``` select ```All traffic```

On ```Source``` select ```Anywhere-Ipv4```

Click on ```Save rules```


**Obtain endpoint**

In your local terminal run:
```
    aws rds describe-db-instances \
        --db-instance-identifier "tophatDiscussionDb" \
        --query 'DBInstances[0].Endpoint'
```

Copy Address of result (DB ENDPOINT)

EXAMPLE: ```tophatdiscussiondb.cyybjsxuimkl.us-west-1.rds.amazonaws.com```

Paste it on ```discussion-api/discussion/db_handler/db_vars.py => ENDPOINT_URL```

```NOTE: Writing variables in this way IS NOT A GOOD IDEA, this is a leak of security.```
```What you would want to do is to create an ENV variable to hold this sensitive information```
```but because this is an excersise we will do it this way.```

**Load MYSQL Dump file to recently created RDS MYSQL Instance**
1:
Open MYSQL Workbench

Add a new MySQL Connection

Give a name to the connection

Paste your DB ENDPOINT from previous step to Hostname textbox

Make sure port is 3306

Paste your Username from previous step to Username textbox

Paste your Password from previous step to Password textbox

Click ```Ok```


2:
Click your recently created Connection

Once connected, Click on ```Server - Data Import```

Click on ```Import from Self-Contained File``` and select ```tophat.sql``` from ```db_schema``` folder in this project

Select tophat_discussion_db on Default Target Schema

Select Dump Structure and Data

Click on ```Start Import```

# Deploy code

Make sure to be at ```discussion-api``` folder

To deploy the code to AWS run:
```
    sam build
```
```
    sam deploy --guided
```

When prompted introduce this values:
```
    Setting default arguments for 'sam deploy'
            =========================================
            Stack Name [sam-app]: discussion-app
            AWS Region [us-west-1]: us-west-1
            #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
            Confirm changes before deploy [y/N]: y
            #SAM needs permission to be able to create roles to connect to the resources in your template
            Allow SAM CLI IAM role creation [Y/n]: y
            #Preserves the state of previously provisioned resources when an operation fails
            Disable rollback [y/N]: y
            StartDiscussionFunction may not have authorization defined, Is this okay? [y/N]: y
            RespondDiscussionFunction may not have authorization defined, Is this okay? [y/N]: y
            RespondCommentFunction may not have authorization defined, Is this okay? [y/N]: y
            AllCommentsFunction may not have authorization defined, Is this okay? [y/N]: y
            Save arguments to configuration file [Y/n]: y
            SAM configuration file [samconfig.toml]:  PRESS ENTER
            SAM configuration environment [default]:  PRESS ENTER
```

After deploying we are ready to test functionallity

Log in into aws console and go to API Gateway menu

Make sure you are in the correct region

click on discussion-app

click on stages

click on Prod

Locate Label Invoke URL and copy the value
EXAMPLE: https://cpa4bggh7c.execute-api.us-west-1.amazonaws.com/Prod

Click on Resources 

Now you can use a tool like postman to test functionallity manually
just append the api endpoint path of each function to the InvokeURL

# Testing

Go to route ```tophat/discussion-api``` and run:
```
    bash setEnvPythonPath.sh
```

To export python path variable to your bashrc


For Integration tests you must replace your API ENDPOINT Invoke URL in the file ```discussion-api/tests/integration/test_vars.py```

**Installing dependencies**

go to ```discussion-api/discussion/`` and run:
```
    pip install -r requirements.txt
```

cd to root folder and you can test running:
```
    pytest -v
```

This will test API endpoints as well as the local code.
```NOTE: For this excercise purpose only. Tests delete all data in the database to recreate testing data```
```Try using the util populate_db.py :)```

# Utils
You can find some utils in ```discussion-api/utils```

```delete_db_info.py``` Will erase all data in the DataBase

```populate_db.py``` Will add some meaningful data to be able to see and manually test with postman

# API DOCUMENTATION

**Function Name: get_all_comments**

**ENDPOINT: ${Invoke URL}/allComments**

**EXAMPLE: https://cpa4bggh7c.execute-api.us-west-1.amazonaws.com/Prod/allComments?question=Do%20you%20have%20pets?**

**Method: GET**
Send querystring parameters to this endpoint

```
    get_all_comments(event, context):
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
```

**Messages**
```
{
    "statusCode": 500,
    "body": {
        "message": "Internal server error"
    }
}

{
    "statusCode": 400,
    "body": {
        "message": "Invalid question. Questions must have text"
    }
}

{
    "statusCode": 400,
    "body": {
        "message": "Invalid question. Question does not exists"
    }
}

{
    "statusCode": 404,
    "body": {
        "message": "No commments available for this discussion"
    }
}

{
    "statusCode": 200,
    "body": {
        "message": "All messages retrieved",
        "comments": ...
    }
}
```


**Function Name: respond_comment**

**ENDPOINT: ${Invoke URL}/respondComment**

**EXAMPLE: https://cpa4bggh7c.execute-api.us-west-1.amazonaws.com/Prod/respondComment**

**Method: POST**

```
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
```

**POST event example**
```
    {
        "comment_id": "2",
        "started_by": "Ryan",
        "response": "That is awesome Clair"
    }
```

**Messages**
```
{
    "statusCode": 500,
    "body": {
        "message": "Internal server error"
    }
}

{
    "statusCode": 400,
    "body": {
        "message": "Invalid comment id. comment id must be a number"
    }
}

{
    "statusCode": 400,
    "body": {
        "message": "Invalid response. Response must have text"
    }
}

{
    "statusCode": 201,
    "body": {
        "message": "Created new response",
        "comment_id" ...
    }
}
```


**Function Name: respond_discussion**

**ENDPOINT: ${Invoke URL}/respondDiscussion**

**EXAMPLE: https://cpa4bggh7c.execute-api.us-west-1.amazonaws.com/Prod/respondDiscussion**

**Method: POST**

```
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
```

**POST event example**
```
    {
        "question": "Do you have pets?",
        "started_by": "Clair",
        "comment": "I have 2 hamsters!"
    }
```

**Messages**
```
{
    "statusCode": 500,
    "body": {
        "message": "Internal server error"
    }
}

{
    "statusCode": 400,
    "body": {
        "message": "Invalid question. Questions must have text"
    }
}

{
    "statusCode": 400,
    "body": {
        "message": "Invalid question. Cannot respond an unexistent discussion"
    }
}

{
    "statusCode": 400,
    "body": {
        "message": "Invalid comment. Comment must have text"
    }
}

{
    "statusCode": 201,
    "body": {
        "message": "Created new response",
        "comment_id" ...
    }
}
```


**Function Name: start_discussion**

**ENDPOINT: ${Invoke URL}/startdiscussion**

**EXAMPLE: https://cpa4bggh7c.execute-api.us-west-1.amazonaws.com/Prod/startdiscussion**

**Method: POST**


```
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
```

**POST event example**
```
    {
        "started_by": "Jason",
        "question": "Do you have pets?"
    }
```

**Messages**
```
{
    "statusCode": 500,
    "body": {
        "message": "Internal server error"
    }
}

{
    "statusCode": 400,
    "body": {
        "message": "Invalid question. Questions must have text"
    }
}

{
    "statusCode": 400,
    "body": {
        "message": "Discussion already exists"
    }
}

{
    "statusCode": 201,
    "body": {
        "message": "Created new discussion",
        "discussion_id" ...
    }
}
```