from socket import *

# ����socket�׽���
tcp_client_socket = socket(AF_INET, SOCK_DGRAM)


def main():
    """TCP�ͻ��˳���"""
    # 1.���ӷ�����
    server_addr = int(input("������IP��"))
    server_port = int(input("������������Ķ˿ڣ�"))
    tcp_client_socket.connect(server_addr, server_port)

    # 2.����/��������
    send_data = input("������Ҫ���͵����ݣ�")
    tcp_client_socket.send(send_data.encode("utf-8"))

    # 3.�ر��׽���
    tcp_client_socket.close()


if __name__ == '__main__':
    main()