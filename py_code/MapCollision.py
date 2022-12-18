import numpy as np
class MapCollision:
    def __init__(self, stage):
        self.wall=np.zeros((240,240))
        self.create_wall()

        #create stage depend on param
        if stage==1:
            self.create_stage1()
        if stage==2:
            self.create_stage2()
    
    #create default collision
    def create_wall(self):
        #left wall
        for i in range(17):
            for j in range(240):
                self.wall[i][j]=1
        #right wall
        for i in range(225,240):
            for j in range(240):
                self.wall[i][j]=1
        #ground
        for i in range(240):
            for j in range(233,240):
                self.wall[i][j]=1

    #create stage 1 collision
    def create_stage1(self):
        #right1
        for i in range(138,201):
            for j in range(196, 202):
                self.wall[i][j]=1

        #right2
        for i in range(138,201):
            for j in range(149, 155):
                self.wall[i][j]=1

        #right3
        for i in range(138,201):
            for j in range(99, 105):
                self.wall[i][j]=1

        #left1
        for i in range(38,102):
            for j in range(175, 180):
                self.wall[i][j]=1
        
        #left2
        for i in range(38,102):
            for j in range(123, 129):
                self.wall[i][j]=1

        #left3
        for i in range(38,102):
            for j in range(73, 79):
                self.wall[i][j]=1

    #create stage 2 collision
    def create_stage2(self):
        #center1
        for i in range(57,183):
            for j in range(202, 207):
                self.wall[i][j]=1

        #center2
        for i in range(57,183):
            for j in range(157, 162):
                self.wall[i][j]=1

        #center3
        for i in range(57,183):
            for j in range(113, 117):
                self.wall[i][j]=1

        #left
        for i in range(17,42):
            for j in range(181, 186):
                self.wall[i][j]=1
        
        #rigth
        for i in range(175, 226):
            for j in range(136, 141):
                self.wall[i][j]=1