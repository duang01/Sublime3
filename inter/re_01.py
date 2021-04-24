import re


def main():

    names = ["191680166@163.com", "hello@163.com", "hello@121.com", "121@163.com", "hello@163.cn", "34567891@163.com", "!#$!@163.com" , "h123h@163.com",
             "hello@qq.com"]

    for name in names:
        ret = re.findall(r"([a-zA-Z_0-9]{4, 20})@(163\.coQQQQQQAm)$", name)

        if ret:
            print(" 邮箱 :%s 符合要求 " % name)

        else:
            print(" 邮箱 :%s 不符合要求" % name)


if __name__ == "__main__":
    main()