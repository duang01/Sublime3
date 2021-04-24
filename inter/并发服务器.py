import socket
import re
import multiprocessing


def service_client(new_socket):
    """为这个客户端返回数据"""

    # 1.接收浏览器发送过来的请求，即http请求
    # GET / HTTP/1.1
    request = new_socket.recv(1024).decode("utf-8")

    request_lines = request.splitlines()
    print("")
    print(">>>*20")
    print(request_lines)

    file_name = ""
    ret = re.match(r"[^/]+(/[^]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)

        if file_name == "/":
            file_name = "/index.html"

    # 返回http格式的数据给浏览器

    try:
        f = open("./html" + file_name, "rb")

    except:
        response = "http/1.1 404 not found!\r\n"
        response += "\r\n"
