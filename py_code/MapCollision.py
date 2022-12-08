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
            for j in range(200, 208):
                self.wall[i][j]=1

        #오른쪽 발판2
        for i in range(138,201):
            for j in range(161, 172):
                self.wall[i][j]=1

        #오른쪽 발판3
        for i in range(138,201):
            for j in range(117, 128):
                self.wall[i][j]=1
        
        #오른쪽 발판4
        for i in range(138,201):
            for j in range(78, 89):
                self.wall[i][j]=1

        #왼쪽 발판1
        for i in range(38,102):
            for j in range(182, 193):
                self.wall[i][j]=1
        
        #왼쪽 발판2
        for i in range(38,102):
            for j in range(138, 149):
                self.wall[i][j]=1

        #왼쪽 발판3
        for i in range(38,102):
            for j in range(94, 105):
                self.wall[i][j]=1
