import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 使用ipv4 ，tcp
t = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 使用ipv4 ,udp


def main():
    # 创建一个udp 套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    udp_socket.bind(("", 8056))

    while True:
        send = input("请输入发送内容：")
        if send == "exit":
            break

        # 使用套接字收发数据  语法：sendto(b"内容", ("ip", port))
        udp_socket.sendto(send.encode("utf-8"), ("192.168.21.65", 7822))

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()