import random
import pygame

# 定义一个屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义一个刷新的帧率
FRAME_PER_SEC = 60
# 定义一个敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 定义英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏 背景精灵"""

    def __init__(self, is_alt=False):

        # 1.调用父类方法实现精灵的创建（image/rect/speed）
        super().__init__("./image/images/background.png")

        # 2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = - self.rect.height

    def update(self):

        # 1.调用父类的方法实现
        super().update()

        # 2.判断是否移出屏幕，如果移出，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = - self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):

        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./image/images/enemy1.png")
        # 2.指定敌机的初始随机速度
        self.speed = random.randint(1, 5)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 1.调用父类方法，保持垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是，需要从精灵组删掉敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，敌机需从精灵组删除")
            self.kill()

    def __del__(self):
        print("敌机挂了...%s" % self.rect)


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):

        # 1.调用父类方法，设置image&speed
        super().__init__("./image/images/me1.png", 0)

        # 2.设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        # 英雄在水平方向移动
        self.rect.x += self.speed

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹...")

        for i in (0, 1, 2):
            # 1.创建子弹精灵
            bullte = Bullet()

            # 2.设置精灵的位置
            bullte.rect.bottom = self.rect.y - i * 20
            bullte.rect.centerx = self.rect.centerx

            # 3.将精灵添加到精灵组
            self.bullets.add(bullte)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):

        # 调用父类方法，设置子弹图片。设置初始速度
        super().__init__("./image/images/bullet1.png", -3)

    def update(self):

        # 调用父类方法，让子弹沿垂直方向发射
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁...")

