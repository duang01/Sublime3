import socket

#客户端

client = socket.socket()                        # 生成一个socket 连接对象
client.connect(("对方的IP地址","端口号"))       #和目标主机建立连接
client.send("发送的消息".encode())               #向对方发送数据
client.close()                                     #关闭连接


# 服务端

server = socket.socket()                             # 生成一个服务端socket对象
server.bind(("ip","端口号"))                           # 绑定监听对象
server.listen()                                      # 监听UDP广播

con,addr = server.accept()                            #等待数据消息    con:ip  addr：端口
print(con,addr)

data = con.recv(1024)                                #接收到的数据   默认1024个字节的大小数据
print("接收到的消息是：",data)
server.close()