import json
class GameStats():
    "跟踪游戏的统计信息"

    def __init__(self,ai_settings):
        "初始化统计信息"
        self.ai_settings =ai_settings
        self.game_active = False
        self.high_score = self.load_score()
        self.reset_stats()

    def reset_stats(self):
        "初始化游戏运行期间可能变化的统计信息"
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_score(self):
        try:
            with open('high_score.json','r') as high_score_obj:
                return json.load(high_score_obj)
        except:
            return 0