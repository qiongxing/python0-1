import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_function as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #设置背景色
    bg_color =(230,230,230)

    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于存储的子弹的编组
    bullets = Group()
    #创建存储外星人的编组
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #创建play按钮
    play_button = Button(ai_settings,screen,"Play")
    #创建存储游戏统计信息实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb =Scoreboard(ai_settings,screen,stats)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets,sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,bullets,aliens,stats,sb)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb)
            #每次循环时重绘屏幕
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,sb)
run_game()