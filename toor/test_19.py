class MusicPlayer:

    def __new__(cls, *args, **kwargs):
        print("创建对象，分配空间")

        # 返回对象的引用
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("播放器初始化")


# 创建一个对象
player = MusicPlayer()

print(player)
