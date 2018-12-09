import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_report():
    #1.组装邮件正文
    msg = MIMEMultipart() #混合格式消息体
    body = MIMEText("python发送的邮件",'plain','utf-8') #plain纯文字html
    msg.attach(body)  #将正文添加到msg对象中
    #2.组装邮件头
    msg['From'] = 'test_results@sina.com'
    msg["To"] = 'wyqingliu0819@163.com'
    msg["Subject"] = "from python"

    #4.附件
    with open("../report/report.html","rb") as f:
        att_file = f.read()

    att = MIMEText(att_file,'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream' # 声明附件的内容格式 MIME数据流格式
    att["Content-Disposition"] = "attachment;filename='report.html'" # 附件描述信息 filename是附件显示的文件名-stream'
    msg.attach(att)

    smtp = smtplib.SMTP_SSL("smtp.163.com")
    smtp.login("ivan-me@163.com","hanzhichao123")
    smtp.sendmail("ivan-me@163.com",
                  'wyqingliu0819@163.com',
                  msg.as_string())