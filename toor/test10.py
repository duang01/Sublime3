'''                     SMTP邮件服务
  准备内容      1.邮件发送方（发送方地址，发送方客户端授权密码，SMTP服务器地址）
                2.邮件内容
                3.邮件接收方

'''

import smtplib
from email.mime.text  import MIMEText


msg_from = "18503091650@163.com"  #发送方
pwd = "Adoung19960423"              # 授权码
to = "191680166@qq.com"        #接收方

subject = "这是python发送的邮件！"
content = "你还没有找女票！抓紧啊.老铁..！"

#构造邮件
msg = MIMEText(content,'plain','utf-8')   #msg邮件对象
msg["Subject"] = subject   #注意首字母大写
msg["From"] = msg_from
msg["To"] = to
'''
#发送邮件
ss = smtplib.SMTP("smtp.163.com",25)
ss.login(msg_from,pwd)
ss.sendmail(msg_from,to,msg.as_string())     #发送
'''
#发送失败
try:
    ss = smtplib.SMTP("smtp.163.com",25)
    ss.login(msg_from,pwd)
    ss.sendmail(msg_from,to,msg.as_string())
    print("发送成功！")

except Exception as  e:
    raise e