import logging
"""
logging.basicConfig(level=logging.ERROR,
                    filename='./log.txt',
                    filemode='a',
                    format='%(asctime)s -%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 日志级别, 开始使用日志
logging.debug("debug信息")
logging.info("通知信息")
logging.warning("警告！！！")
logging.error("程序错误！！！")
logging.critical("程序崩溃！！！")
"""

# 第一步 创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 第二步，创建一个handler，用于写入日志文件
logfile = './log.txt'
fh = logging.FileHandler(logfile, mode='a')  # 追加log到log.txt文件
fh.setLevel(logging.DEBUG)                   # 输出file的log等级开关

# 第三步， 在创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)                  # 输出到控制台的log等级总开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter("'%(asctime)s -%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

# 第六步，日志信息
logging.debug("debug信息")
logging.info("通知信息")
logging.warning("警告！！！")
logging.error("程序错误！！！")
logging.critical("程序崩溃！！！")
