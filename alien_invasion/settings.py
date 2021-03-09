class Settings():
    """存储游戏所有设置的类"""

    def __init__(self):
        #屏幕设置
        self.screen_width= 1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        #飞船的设置
        self.ship_speed_factor=1.5
        self.ship_limit = 3
        #子弹设置
        self.bullet_speed_factory = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3
        #外星人设置
        self.alien_speed_factor = 1
        #向下移动的速度
        self.fleet_drop_speed = 10
        #fleet_direction表示1向右移，-1左移
        self.fleet_direction=1