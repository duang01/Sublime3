"""
个税计算器
个人所得税计算公式
应纳税所得额 = 工资收入金额 - 各项社会保险费 - 起征点（5000）
应纳税额 = 应纳税所得额*税率 - 速算扣除数
"""
before=float(input("请输入你的税前工资："))

if before <=0:
    print("请输入正确的税前工资！！！谢谢呐@-@")
elif before - 5000 <= 0:
    print("您不需要缴纳个人所得税，请努力加油哟！！！")
else:
    m1 = float(input("请输入你的社保扣除金额："))
    ss = 0  #定义纳税金额
    ys = before - m1 - 5000  #定义应纳税所得额

    if ys <= 3000 and ys > 0:
        ss = ys * 0.03 - 0
    elif ys <= 12000:
        ss = ys * 0.10 - 210
    elif ys <= 25000:
        ss = ys * 0.20 - 1410
    elif ys <= 35000:
        ss = ys * 0.25 - 2660
    elif ys <= 55000:
        ss = ys * 0.30 - 4410
    elif ys <= 80000:
        ss = ys * 0.35 - 7160
    else:
        ss = ys * 0.45 - 15160


    print("您应纳税金额:" ,ss , "到手工资为:",before - m1 - ss)


