import pymysql
import csv
import os,time,datetime
from openpyxl import load_workbook
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
from email import encoders
from email.header import Header

"""
导入连接MySQL需要的包，没有安装pymysql需要先安装
使用命令行切换到python的安装路径下的scripts子目录下安装（pip install pymysql）
"""
#连接MySQL数据库
conn = pymysql.Connect(
    host='localhost',
    user='root',
    password='root',
    port =3306,
    db='local_db',
    charset='utf8'
)
#使用cursor()方法获取操作游标
cursor1 = conn.cursor()
#使用execute()方法执行sql语句
#sql = 'select IPCIP from ipcconfig'  #通过sql语句，筛选符合要求的数据库表数据
sql = "select IPCIP from ipcconfig where ServerIP='10.4.201.25'"  #通过sql语句，筛选符合要求的数据库表数据,10路。
cursor1.execute(sql)
#使用fetchone()方法获取所有数据
results = cursor1.fetchall()

ip_list=[]
i=2
count=0
count_False=0
count_True=0
start_Time=time.time()
for i in range(len(list(results))):
    ip=results[i][0]
    return1 = os.system('ping -c 3 %s' % ip)
    if return1:
        #print('ping %s is fail' % ip)
        count_False += 1
        ip_list.append(ip)
    else:
        #print('ping %s is ok' % ip)
        count_True += 1
    count+=1
    #print('处理第 %s 个摄像头'% count)
end_Time = time.time()
nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print('当前时间：',nowtime)
print("处理时间 % s 秒"% (end_Time-start_Time))
print("ping通的ip数：", count_True)
print("ping不通的ip数：", count_False)

if count_False>=1:
    #如果有一个IP不通，杀死所有进程
    os.system('ps -ef | grep n_main | grep -v grep |cut -c 9-15|xargs kill -9')
    #如果有一个ip不通，则进行邮件提醒，并且重启系统
    mailserver = "smtp.163.com"  #邮箱服务器地址
    username_send = 'meiling_1948@163.com'  #邮箱用户名
    password = 'RAXUBCKRYJPWPFRL'   #邮箱密码：需要使用授权码
    username_recv = ['xxx','xxx'] #收件人，多个收件人用逗号隔开
    mail = MIMEText('12路 服务器IP：x.x.x.x'+'\n摄像头出现问题请及时处理'+str(ip_list))
    mail['Subject'] = '警告警告'
    mail['From'] = username_send  #发件人
    mail['To'] = Header(','.join(username_recv))
    smtp = smtplib.SMTP(mailserver,port=25) # 连接邮箱服务器，smtp的端口号是25

    smtp.login(username_send,password)  #登录邮箱
    smtp.sendmail(username_send,username_recv,mail.as_string())# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
    smtp.quit() # 发送完毕后退出smtp
    print ('mail send success')

    #发送邮件提醒2min后，重启系统
    #time.sleep(120)
    #command = "sudo reboot"
    #password = 'fsym123456'
    #os.system('echo %s | sudo -S %s' % (password, command))
