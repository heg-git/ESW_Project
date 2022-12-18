from PIL import Image
import numpy as np
class Boss:
    def __init__(self):
        self.state = None
        self.size = (55, 55)
        self.image = Image.open("./res/boss/boss_left_1.png").resize(self.size)
        self.position = np.array([170, 176, 225, 231])
        self.speed = 3
        self.move_count = 0
        self.up_down_count = 0
        self.flag = 0
        self.hp = 30
    
    #boss move
    def move(self):
        #return if boss is bubbled
        if self.state == "bubbled":
            return
        #move left
        if self.move_count < 52:
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
                #boss go up if up_down_count < 5
                if self.up_down_count<5:
                    self.position[1] -= 1
                    self.position[3] -= 1 
                #boss go down if up_down_count >= 5
                else:
                    self.position[1] += 1
                    self.position[3] += 1
        
        elif self.move_count == 52:
            self.up_down_count +=1
        
        #move right
        elif self.move_count < 104:
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
                #boss go up if up_down_count < 5
                if self.up_down_count<5:
                    self.position[1] -= 1
                    self.position[3] -= 1  
                #boss go down if up_down_count >= 5
                else:
                    self.position[1] += 1
                    self.position[3] += 1
        #init move_count
        else:
            self.up_down_count += 1
            if self.up_down_count == 10:
                self.up_down_count = 0
            self.move_count=0

        self.move_count+=1
    
    #bubble hit
    def bubbled(self):
        if self.hp==0:
            if self.move_count < 52:
                self.image = Image.open("./res/boss/boss_left_bubbled.png").resize(self.size)
            else:
                self.image = Image.open("./res/boss/boss_right_bubbled.png").resize(self.size)
            self.state="bubbled"
        self.hp-=1
        