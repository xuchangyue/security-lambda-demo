# IAM Access Denied Responder
This example solution will setup an automated response to an access denied event that occurs within a CloudTrail event, a Failed authentication attempt to the AWS console, or a Client.UnauthorizedOperation event occurs.

本示例模板会创建当Access Denied Event发生时的自动响应。例如当控制台失败后，会有警报消息通知到Chime，包含具体事件，源IP的地理位置和Owner，并把尝试登陆的用户的操作记录和相关Cloudtrail日志调取出来。源IP的GEO和Owner信息通过调用Whois的API得到。
## 架构
![incident response architecture](incident-response-architecture.png)

## 启动模板
1. 保证模板目标区域有开启CloudTrail。
2. 将Lambda代码打包。 参考[the AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html). 
3. 将Lambda ZIP上传到S3桶中。
4. 启动CloudFormation模板AccessDeniedRespones.yaml，并按照参考描述填写参数。（调取Whois API查询IP的GEO和Owner信息需要提供Whois的API key，需注册Whois账号，每月有500次的免费调用额度）
