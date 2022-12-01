import numpy as np
class MapCollision:
    def __init__(self):
        self.wall=np.zeros((240,240))
        self.create_wall()
        # self.collision1

    def create_wall(self):
        #왼쪽 기둥
        for i in range(17):
            for j in range(240):
                self.wall[i][j]=1
        #오른쪽 기둥
        for i in range(225,240):
            for j in range(240):
                self.wall[i][j]=1
        #땅
        for i in range(240):
            for j in range(233,240):
                self.wall[i][j]=1
        #가운데 기둥1
        for i in range(60,186):
            for j in range(198, 201):
                self.wall[i][j]=1
        # for i in range(240):
        #     for j in range(240):
        #         print(map[i][j],end='')
        #     print("")