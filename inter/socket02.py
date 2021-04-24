import socket


def main():
    # 1.创建套接字用于接收数据
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定用于接收数据的IP及port
    localadds = ("192.168.22.53", 7788)
    udp_socket.bind(localadds)
    # 3.接收数据并用变量保存
    while True:
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]
        seed_addr = recv_data[1]
        print("%s:%s" % (str(seed_addr), recv_msg.decode("gbk")))
        # 4.关闭套接字
        udp_socket.close()


if __name__ == '__main__':
    main()