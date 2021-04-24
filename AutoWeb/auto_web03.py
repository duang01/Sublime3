"""
需求：
    1、设计一个Game类
    2、属性：
        1.定义一个类属性 top_score 记录游戏的最高分
        2.定义一个实例属性 player_name 记录当前游戏的玩家姓名
    3、方法：
        1.静态方法 show_help 显示游戏的帮助信息
        2.类方法 show_top_score 显示历史最高分
        3.实例方法 start_game 开始当前玩家的游戏
    4、主程序步骤：
        1.查看帮助信息
        2.查看历史最高分
        3.创建游戏对象，开始游戏
"""


class Game(object):
    # 设置类属性
    top_score = 0

    # 初始化实例属性
    def __init__(self, play_name):
        self.play_name = play_name

    # 静态方法 show_help 显示游戏的帮助信息
    @staticmethod
    def show_help():
        print("这是游戏的帮助信息")

    # 类方法 show_top_score 显示历史最高分
    @classmethod
    def show_top_score(cls):
        print("历史最高分为：%d" % cls.top_score)

    # 实例方法 start_game 开始当前玩家的游戏
    def start_game(self):
        print("欢迎 %s 玩家进入游戏" % self.play_name)


# 1.查看帮助信息
Game.show_help()

# 查看历史最高分
Game.show_top_score()

# 创建游戏对象
gameer = Game("王五")

# 开始游戏
gameer.start_game()


