from random import choice

class RandomWalk():
    """一个生成随机漫步的类"""

    def __init__(self,num_points=5000):
        """初始化随机漫步"""
        self.num_points = num_points
        #所有随机漫步都始于(0,0)
        self.x_values=[0]
        self.y_values=[0]

    def fill_walk(self):
        "计算随机漫步含有的所有点"
        while len(self.x_values) <self.num_points:
            #决定前进方向和前进距离
            x_step = self.get_step()
            y_step =  self.get_step()

            #拒绝原地踏步
            if x_step == 0 and y_step ==0:
                continue

            #就算下一个点的x，y
            next_x = self.x_values[-1] +x_step
            next_y = self.y_values[-1] +y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

            
    def get_step(self):
        "计算行走方向以及步数"
        wall_direction =choice([1,-1])
        wall_distance =choice([0,1,2,3,4,5,6,7,8])
        wall_step = wall_direction*wall_distance
        return wall_step