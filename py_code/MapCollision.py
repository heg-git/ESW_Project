import numpy as np
class MapCollision:
    def __init__(self, stage):
        self.wall=np.zeros((240,240))
        self.create_wall()
        if stage==1:
            self.create_stage1()
        if stage==2:
            self.create_stage2()
    
    def create_wall(self):
        #왼쪽 벽
        for i in range(17):
            for j in range(240):
                self.wall[i][j]=1
        #오른쪽 벽
        for i in range(225,240):
            for j in range(240):
                self.wall[i][j]=1
        #바닥
        for i in range(240):
            for j in range(233,240):
                self.wall[i][j]=1

    def create_stage1(self):
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

    def create_stage2(self):
        #가운데 발판1
        for i in range(57,183):
            for j in range(202, 207):
                self.wall[i][j]=1

        #가운데 발판2
        for i in range(57,183):
            for j in range(157, 162):
                self.wall[i][j]=1

        #가운데 발판3
        for i in range(57,183):
            for j in range(113, 117):
                self.wall[i][j]=1

        #왼쪽 발판
        for i in range(17,42):
            for j in range(181, 186):
                self.wall[i][j]=1
        
        #오른쪽 발판
        for i in range(175, 226):
            for j in range(136, 141):
                self.wall[i][j]=1