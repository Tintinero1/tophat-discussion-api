# tophat-discussion-api


# Deploy

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

example: ```tophatdiscussiondb.cyybjsxuimkl.us-west-1.rds.amazonaws.com```


# Testing

Go to route ```tophat/discussion-api``` and run:
```
    bash setEnvPythonPath.sh
```

To export python path variable to your bashrc