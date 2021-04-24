import socket


def main():

    # 1.�����׽���
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.��IP��port
    tcp_server_socket.bind("", 7988)

    # 3.��Ĭ�ϵ��׽�����������Ϊ���� listen
    tcp_server_socket.listen(128)

    while True:  # ѭ��Ϊ����ͻ��˷���
        print("�ȴ�һ���µĿͻ��˵ĵ���������")
        # 4.�ȴ��ͻ��˵�����accept
        new_client_socket, client_addr = tcp_server_socket.accept()
        print(client_addr)  # �ͻ��˵�IP��port

        while True:  # ѭ��Ϊͬһ���ͻ��˷�����

            # 5.recv/send ���շ�������
            recv_data = new_client_socket.recv(1024)
            print("�ͻ��˷��͹����������ǣ�%s" % recv_data.decode("utf-8"))  # ���յ��Ŀͻ��˵����ݣ���С1024 kb

            # �ж�recv����������֣�
            # 1. �ͻ��˷��͹���������
            # 2. �ͻ��˵�����close ������
            if recv_data:
                # ����һ�������ݸ��ͻ���
                new_client_socket.send("���͵�����".encode("utf-8"))

            else:
                break

        # �ر��׽���
        new_client_socket.close()
        print("�Ѿ�Ϊ����ͻ��˷������...")

    tcp_server_socket.close()


if __name__ == '__main__':
    main()