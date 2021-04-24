import pygame


pygame.init()

# 创建游戏窗口 480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 加载图像数据
bg = pygame.image.load("./image/images/background.png")

# 绘制图像 blit
screen.blit(bg, (0, 0))


# 绘制英雄的飞机
hero = pygame.image.load("./image/images/me1.png")
screen.blit(hero, (150, 300))

# 更新屏幕
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect 记录飞机初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

while True:

    # 设置刷新频率
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():
        # print(event)

        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出0.0..")

            # quit 卸载所有的模块
            pygame.quit()

            # exit（） 直接终止当前正在执行的程序
            exit()

    # 修改飞机的位置
    hero_rect.y -= 1

    if hero_rect.y <= 0:
        hero_rect.y = 700

    # 调用blit绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

pygame.quit()
