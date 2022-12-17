from PIL import Image
import numpy as np
class Boss:
    def __init__(self):
        self.state = None
        self.size = (55, 55)
        self.image = Image.open("./res/boss/boss_left_1.png").resize(self.size)
        self.position = np.array([170, 176, 225, 231])
        self.speed = 3
        self.life = 30
        self.move_count = 0
        self.up_down_count = 0
        self.flag = 0
        
        
        #self.direction = "left"
        #self.distance = int(distance/2)
        self.hp = 30
        
    def move(self):
        if self.state == "bubbled":
            return
        if self.move_count < 52:
            #print(self.move_count)
            if self.flag < 5:
                self.image = Image.open("./res/boss/boss_left_1.png").resize(self.size)
            elif self.flag<10:
                self.image = Image.open("./res/boss/boss_left_2.png").resize(self.size)
            else:
                self.flag = -1
            self.flag += 1
            self.position[0] -= self.speed
            self.position[2] -= self.speed
            if self.move_count%2==1:
                if self.up_down_count<5:
                    self.position[1] -= 1
                    self.position[3] -= 1  
                else:
                    self.position[1] += 1
                    self.position[3] += 1

        elif self.move_count == 52:
            self.up_down_count +=1

        elif self.move_count < 104:
            #print(self.move_count)
            if self.flag < 5:
                self.image = Image.open("./res/boss/boss_right_1.png").resize(self.size)
            elif self.flag<10:
                self.image = Image.open("./res/boss/boss_right_2.png").resize(self.size)
            else:
                self.flag = -1
            self.flag += 1
            self.position[0] += self.speed
            self.position[2] += self.speed
            if self.move_count%2==1:
                if self.up_down_count<5:
                    self.position[1] -= 1
                    self.position[3] -= 1  
                else:
                    self.position[1] += 1
                    self.position[3] += 1
        
        else:
            self.up_down_count += 1
            if self.up_down_count == 10:
                self.up_down_count = 0
            self.move_count=0

        self.move_count+=1
    
    def bubbled(self):
        if self.life==0:
            self.state="bubbled"
        self.life-=1
        