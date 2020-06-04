Summary
========
Amazon CloudWatch Events trigger this check when AWS CloudTrail logs EC2 API calls. Specifically, Amazon CloudWatch Events Rules monitoring AWS CloudTrail Logs, trigger based on an API call for "RunInstances". The trigger invokes AWS Lambda which runs the python script attached. The python script evaluates the instances's ami if is the required ami, if not, the instances will be terminated, and a chime message will be sent to the chime user.

Deployment
==========

To deploy this security control, upload the security control Lambda ZIP file to a location in Amazon S3. This location must be in the same region you intend to deploy the control.

Launch the provided AWS CloudFormation template using the AWS Console and provide the following information:

  | Parameter            | Description
  | -------------------- | --------------------------------------------------------------------------------------------------
  | S3 Bucket            | The S3 bucket name you uploaded the Lambda ZIP to
  | S3 Key               | The S3 location of the Lambda ZIP. No leading slashes. (ex. Lambda.zip or controls/lambda.zip. )
  | Chime Hook URL       | The Chime webhook to send a message
  | Chime User Login     | The user login to notify @
  | Required AMI id      | The AMI id forced to use
