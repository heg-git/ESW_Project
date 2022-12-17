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

        #오른쪽 발판1
        for i in range(138,201):
            for j in range(196, 202):
                self.wall[i][j]=1

        #오른쪽 발판2
        for i in range(138,201):
            for j in range(149, 155):
                self.wall[i][j]=1

        #오른쪽 발판3
        for i in range(138,201):
            for j in range(99, 105):
                self.wall[i][j]=1

        #왼쪽 발판1
        for i in range(38,102):
            for j in range(175, 180):
                self.wall[i][j]=1
        
        #왼쪽 발판2
        for i in range(38,102):
            for j in range(123, 129):
                self.wall[i][j]=1

        #왼쪽 발판3
        for i in range(38,102):
            for j in range(73, 79):
                self.wall[i][j]=1
