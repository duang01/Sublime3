import socket


def main():
    # 1.�����׽������ڽ�������
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.�����ڽ������ݵ�IP��port
    localadds = ("192.168.22.53", 7788)
    udp_socket.bind(localadds)
    # 3.�������ݲ��ñ�������
    while True:
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]
        seed_addr = recv_data[1]
        print("%s:%s" % (str(seed_addr), recv_msg.decode("gbk")))
        # 4.�ر��׽���
        udp_socket.close()


if __name__ == '__main__':
    main()