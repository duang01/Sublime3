# A股提醒系统   @接口 Tushare

import tushare as ts
import time
import smtplib
from email.mime.text import MIMEText

#while 1==1:
def getrealtimedata(share):                #获取股票数据
    dataNow = ts.get_realtime_quotes(share.code)

    share.name = dataNow.loc[0][0]                            #  股票名字
    share.price = float(dataNow.loc[0][3])                    #  股票价格
    share.high = dataNow.loc[0][4]                            #  当日最高价
    share.low = dataNow.loc[0][5]                             #  当日最低价
    share.volum = dataNow.loc[0][8]                           #  成交量
    share.amount = dataNow.loc[0][9]                          #  成交额
    share.openToday = dataNow.loc[0][1]                       #  开盘价
    share.pre_close = dataNow.loc[0][2]                       #  收盘价
    share.timee = dataNow.loc[0][30]                          #  日期
    #share.describe = "股票名字:",share.name,"股票价格:",share.price,"当日最高价:",\
    #                 share.high,"当日最低价：",share.low,"成交量：",share.volum,"成交额：",\
    #                share.amount,"开盘价：",share.openToday,"收盘价：",share.pre_close,"交易日期：",share.timee
    share.describe = "股票名字:"+share.name, "股票价格:"+ str(share.price),"当日最高价:"+share.high,"当日最低价："+share.low,"成交量："+share.volum,"日期:"+str(share.timee)
    return share

    #print("股票名字:",name,"股票价格:",price,"当日最高价:",high,"当日最低价：",low,"成交量：",volum,"成交额：",amount,"开盘价：",openToday,"收盘价：",pre_close,"交易日期：",timee)
    #print(dataNow)
'''
def sendmail(subject,content):
    msg_from = "18503091650@163.com"
    pwd = "Adoung19960423"
    to = "191680166@qq.com"



    msg = MIMEText(content,'plain','utf-8')
    msg["Subject"] = subject
    msg["From"] = msg_from
    msg["To"] = to

    try:
        ss = smtplib.SMTP("smtp.163.com",25)
        ss.login(msg_from,pwd)
        ss.sendmail(msg_from,to,msg)
        print("发送成功！")
    except Exception as E:
        print("发送失败！详情：",E)



'''


#定义一个股票类
class Share():
    def __init__(self,code,buy,sale):
        self.name = ""
        self.price = ""
        self.high = ""
        self.low = ""
        self.volum = ""
        self.amont = ""
        self.openToday = ""
        self.pre_close = ""
        self.timee = ""
        self.describe = ""                     #描述信息
        self.code = code                       #股票代码
        self.buy = buy
        self.sale = sale


def main(sharelist):
    for share in sharelist:

        sss = getrealtimedata(share)
        print(sss.describe)



        if sss.price <= sss.buy:
            print("达到买点，注意操作机会！买点价为：",share.buy)
            #sendmail("达到买点",share.describe)
        elif sss.price >=sss.sale:
            print("达到卖点，注意关注信号！！！卖点价为：",share.sale)
            #sendmail("达到卖点",share.describe)
        else:
            print("保持持仓中。。。")

while 1==1:

    share1 = Share("600106",3.1,3.20)
    share2 = Share("601988", 3.5, 3.8)
    share3 = Share("000591", 3.2, 3.5)

    list1 = [share1,share2,share3]
    print("--------------------------------------------")
    main(list1)
    time.sleep(300)
