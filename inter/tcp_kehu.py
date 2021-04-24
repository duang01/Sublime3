from socket import *

# 创建socket套接字
tcp_client_socket = socket(AF_INET, SOCK_DGRAM)


def main():
    """TCP客户端程序"""
    # 1.连接服务器
    server_addr = int(input("请输入IP："))
    server_port = int(input("请输入服务器的端口："))
    tcp_client_socket.connect(server_addr, server_port)

    # 2.发送/接收数据
    send_data = input("请输入要发送的数据：")
    tcp_client_socket.send(send_data.encode("utf-8"))

    # 3.关闭套接字
    tcp_client_socket.close()


if __name__ == '__main__':
    main()