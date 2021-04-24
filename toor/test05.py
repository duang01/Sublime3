'''
  模拟银行存取款
            --2019.06.26

                                            《需求文档》
            01.模拟银行存取款；
                a.模拟三张银行卡，1001，1002，1003 ，分别设置密码和余额（可以用9个变量分别保存卡号，密码，余额）
                b.提示用户输入银行卡卡号和密码
                c.如果用户输入正确--提示用户取款，存款，还是退出，并提示余额多少。输入错误--重新输入卡号和密码
                d.选择取款 -- 提示输入取款金额，如果超过余额，提示余额不足。否则在余额上扣除相应金额（整百）
                e.选择存款 -- 输入存款金额，余额加上存款金额并提示当前余额多少
                f.选择退出 -- 重新输入卡号和密码
                g.设置3次输入错误账号密码，提示银行卡已被锁定

'''
#定义三张卡信息

card1 = "1001"
pwd1 = "123456"
ban1 = "10000"

card2 = "1002"
pwd2 = "123456"
ban2 = "10000"


card3 = "1003"
pwd3 = "123456"
ban3 = "10000"

print("欢迎来到python银行")
times = 0
while True:

    card = input("请输入您的卡号：！")
    pwd = input("请输入您的密码:")
    ban = 0


    if card == card1 and pwd == pwd1:
        ban = ban1
        print("您当前账户余额为：",ban1 )


    elif card == card2 and pwd == pwd2:
        ban = ban2
        print("您当前账户余额为：", ban2 )


    elif card == card3 and pwd == pwd3:
        ban = ban3
        print("您当前账户余额为：", ban3 )


    else:
        times = times+1
        if times >= 3:
            print("您已输错3次错误账号或密码，请联系人工柜台！！！")
            break
        else:
            print("您输入的卡号或密码输入有误！请重新输入！")
            continue


    while True:
        num = input("请输入要办理的业务：1.存款 2.取款 3.退卡")
        if num == "1":
            inn = float(input("请输入您的存款金额："))
            if inn <=0 :
                print("存款金额需大于0！！！")
                continue
            elif inn >0 :
                ban = float(ban) + inn
                print("存款成功！存入金额为：",inn,"总余额为：",ban)



        elif num == "2":
            out = float(input("请输入您的取款金额："))
            if out > float(ban):
                print("余额不足，请继续努力！！！")
                continue

            else:
                ban = float(ban) - out
                print("取款成功！取出金额为：",out,"取后余额为：",ban)



        elif num == "3":
            print("请您保管好您的卡片！")
            print("谢谢！欢迎下次光临！爱你哟，么么哒。")
            break

        else:
            print("您的输入有误，请重新输入！")
            continue