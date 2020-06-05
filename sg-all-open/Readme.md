概要
========
Amazon CloudWatch Events规则会监控EC2 API "AuthorizeSecurityGroupIngress"的调用，当被调用时会触发Lambda函数，Lambda函数会评估安全组的源IP和CIDR地址块范围。 如果CIDR是0.0.0.0/0或::/0, Lambda会发布警告信息给SNS topic，订阅此topic的邮箱会收到警告邮件。

部署
==========
讲Lambda代码打包，上传到部署此模板同区域的S3桶中。
启动CloudFormation模板，填入以下参数。
  | Parameter            | Description
  | -------------------- | --------------------------------------------------------------------------------------------------
  | S3 Bucket            | 存放Lambda ZIP的S3桶
  | S3 Key               | Lambda ZIP的S3 Key，例如Lambda.zip或controls/lambda.zip
  | Notification Email   | 接收警告邮件的邮箱地址
  | Logging Level        | 日志级别， INFO应只用来debug
