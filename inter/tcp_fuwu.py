import socket


def main():

    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定IP和port
    tcp_server_socket.bind("", 7988)

    # 3.让默认的套接字由主动变为被动 listen
    tcp_server_socket.listen(128)

    while True:  # 循环为多个客户端服务
        print("等待一个新的客户端的到来。。。")
        # 4.等待客户端的链接accept
        new_client_socket, client_addr = tcp_server_socket.accept()
        print(client_addr)  # 客户端的IP和port

        while True:  # 循环为同一个客户端服务多次

            # 5.recv/send 接收发送数据
            recv_data = new_client_socket.recv(1024)
            print("客户端发送过来的请求是：%s" % recv_data.decode("utf-8"))  # 接收到的客户端的数据，大小1024 kb

            # 判断recv解堵塞有两种，
            # 1. 客户端发送过来的数据
            # 2. 客户端调用了close 导致了
            if recv_data:
                # 回送一部分数据给客户端
                new_client_socket.send("发送的数据".encode("utf-8"))

            else:
                break

        # 关闭套接字
        new_client_socket.close()
        print("已经为这个客户端服务完毕...")

    tcp_server_socket.close()


if __name__ == '__main__':
    main()