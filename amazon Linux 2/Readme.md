概要
========
Amazon CloudWatch Events规则会监控EC2 API "RunInstances"的调用，当被调用时会触发Lambda函数，Lambda函数会检查启用实例使用的AMI Id是否和强制使用的AMI Id一致，如果不一致则降实例终止并chime通知用户。

部署
==========
讲Lambda代码打包，上传到部署此模板同区域的S3桶中。
启动CloudFormation模板，填入以下参数。
  | Parameter            | Description
  | -------------------- | --------------------------------------------------------------------------------------------------
  | S3 Bucket            | 存放Lambda ZIP的S3桶
  | S3 Key               | Lambda ZIP的S3 Key，例如Lambda.zip或controls/lambda.zip
  | Chime Hook URL       | Chime room的Webhook URL
  | Chime User Login     | 需要@提醒的用户login
  | Required AMI Id      | 强制使用的AMI Id
