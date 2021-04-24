from distutils.core import setup

setup(name="home", version="1.0",
      description="itheima's 发送和请求模块",
      long_description="完整的发送和接收模块",
      author="李正鹏", author_email="191680166@qq.com",
      url="www.baidu.com",
      py_modules=["home.send_message",
                  "home.receive_message"])


"""
制作压缩包发布：
            1.建立setup.py文件。如上
            2.构建准备模块  终端 $python3 setup.py build
            3.生成发布压缩包 终端 $python3 setup.py sdist
            
     收到压缩包：安装模块
            1.tar -zxvf home-1.0.tar.gz
            2.sudo python3 setup.py install
            3.       

"""