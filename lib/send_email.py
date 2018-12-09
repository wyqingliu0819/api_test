import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from conf import config

def send_report():
    #1.组装邮件正文
    msg = MIMEMultipart() #混合格式消息体
    body = MIMEText("python发送的邮件",'plain','utf-8') #plain纯文字html
    msg.attach(body)  #将正文添加到msg对象中
    #2.组装邮件头
    msg['From'] = config.smtp_user
    msg["To"] = config.receiver
    msg["Subject"] = config.subject

    #4.附件
    with open(config.report_file,"rb") as f:
        att_file = f.read()

    att = MIMEText(att_file,'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream' # 声明附件的内容格式 MIME数据流格式
    att["Content-Disposition"] = "attachment;filename='report.html'" # 附件描述信息 filename是附件显示的文件名-stream'
    msg.attach(att)

    smtp = smtplib.SMTP_SSL(config.smtp_server)
    smtp.login(config.smtp_user,config.smtp_password)
    smtp.sendmail(config.smtp_user,
                  config.receiver,
                  msg.as_string())