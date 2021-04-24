'''第二天学习
快递价格计算器
'''
i=1

while 1==1:

    print("欢迎来到快递系统！您是第",i,"位顾客")

    weight = int(input("请输入重量（kg）:"))
    num = input("请输入地点编号（01.其他 02.东三省/宁夏/青海/海南 03.新疆/西藏 04.港澳台/国外）：")
    p=0
    if weight>=3:
        if num == "01":
            p=10+5*(weight-3)

        elif num == "02":
            p=12+10*(weight-3)

        elif num == "03":
            p=20+20*(weight-3)

        elif num == "04":
            p=666666
            print("不接受寄件，请联系客服。谢谢！")

        else:
            print("输入错误!!!请输入数字，谢谢！")
            continue

    elif weight<3 and weight>0:
        if num == "01":
            p=10

        elif num == "02":
            p=12

        elif num == "03":
            p=20

        elif num == "04":
            p = 888888
            print("不接受寄件，抱歉！")
        else:
            print("输入错误!!!请输入数字，谢谢！")
            continue

    else:
        print("输入错误!!!请输入数字，谢谢！")

    print("您好，此件包裹的快递费用为:",p,"元！")
    i = i + 1