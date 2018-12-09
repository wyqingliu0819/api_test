import logging
import os

#数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_passwd = '123456'
db_db = 'api_test'
db_charset='utf8'

#路径配置
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#数据文件目录
data_path = os.path.join(project_path, 'data')
data_file = os.path.join(project_path,'data','data.xlsx')
log_file = os.path.join(project_path,'log','log.txt')
report_file = os.path.join(project_path, 'report', 'report.html')

#日志文件

#邮件配置
smtp_server = 'smtp.163.com'
smtp_user = 'ivan-me@163.com'
smtp_password = 'hanzhichao123'

receiver = 'wyqingliu0819@163.com'
subject = '接口测试报告'
body = 'hi,all,\n附件中是接口测试报告,请查收.'

is_send_report = True
#log配置
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    filemode="a"
                    )

if __name__ == '__main__':
    # logging.info("hello, world")
    # logging.info("中文日志")
    print(data_file,'\n', log_file,'\n',report_file)
    print()