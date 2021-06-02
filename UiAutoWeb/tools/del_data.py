import os


class DelData:

    path = ""
    # 删除文件方法

    def del_file(self, path):
        if os.path.isfile(path):
            os.remove(path)
            return os.path.exists(path)
        else:
            os.removedirs(path)
            return os.path.exists(path)

