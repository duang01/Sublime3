# 定义函数
import os

import yaml

from UiAutoWeb.config import BASE_PATH


def read_yaml(filename):
    # 组装文件路径
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    # 定义一个空列表，用来组装测试数据
    arrs = []
    # 获取文件流
    with open(file_path, "r", encoding="utf-8") as f:

        # 遍历 调用yaml.safe_load(f).value()方法
        for datas in yaml.safe_load(f).values():
            arrs.append(tuple(datas.values()))

    # 返回结果
    return arrs


