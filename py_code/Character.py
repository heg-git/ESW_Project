import numpy as np
from PIL import Image, ImageDraw
from BubbleManager import BubbleManager

class Character:
    def __init__(self):
        self.appearance = "character"
        self.state = None
        self.position = [70, 0, 95, 25]
        self.size = (25,25)
        self.image = Image.open("./res/character/ch_right_1.png").resize(self.size)
        self.flag = 0
        self.count = 0
        self.direction = "right"
        self.gravity = 5
        self.life = 3
        self.bubble_manager = BubbleManager()
        self.bubble=[]
        self.i=0

    def move(self, command):
        if command == "left":
            self.direction = "left"
            self.flag = 0 if self.flag else 1
            if self.flag:
                self.image = Image.open("./res/character/ch_left_1.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_left_2.png").resize(self.size)
            self.position[0] -= 5
            self.position[2] -= 5
                
        elif command == "right":
            self.direction = "right"
            self.flag = 0 if self.flag else 1
            if self.flag:
                self.image = Image.open("./res/character/ch_right_1.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_right_2.png").resize(self.size)
            self.position[0] += 5
            self.position[2] += 5
        
        elif command == "up":
            self.direction = "left"
            self.flag = 0 if self.flag else 1
            if self.flag:
                self.image = Image.open("./res/character/ch_left_1.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_left_2.png").resize(self.size)
            self.position[1] -= 5
            self.position[3] -= 5

    def jump(self):
        if self.count < 8:
            if self.direction=="right":
                self.image = Image.open("./res/character/ch_right_jump.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_left_jump.png").resize(self.size)
            
            self.position[1] -= self.gravity
            self.position[3] -= self.gravity
            #self.gravity -= 1
            self.count += 1


        elif self.count < 16:
            if self.direction=="right":
                self.image = Image.open("./res/character/ch_right_down.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_left_down.png").resize(self.size)
            
            #self.gravity+=1
            self.position[1] += self.gravity
            self.position[3] += self.gravity
            self.count+=1

        else:
            if self.direction=="right":
                self.image = Image.open("./res/character/ch_right_1.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_left_1.png").resize(self.size)
            self.count=0
            self.state = None
        
    def attack(self):
        if len(self.bubble_manager.bubble_pool.bubble)==0:
            self.bubble_manager.create_bubble()
        else:
            print(len(self.bubble))
            self.bubble.append(self.bubble_manager.get_bubble())

        if self.direction=="right":
            self.image = Image.open("./res/character/ch_right_attack.png").resize(self.size)
            self.bubble[-1].position = [self.position[2], self.position[1]+3, self.position[2]+15, self.position[1]+18]
            self.bubble[-1].direction = "right"
        else:
            self.image = Image.open("./res/character/ch_left_attack.png").resize(self.size)
            self.bubble[-1].position = [self.position[0]-15, self.position[1]+3, self.position[0], self.position[1]+18]
            self.bubble[-1].direction = "left"


    def mov_bubble(self):
        self.bubble_manager.mov_bubble(self.bubble)

    def colision_check(self, collision):
        #땅 체크 
        if(collision.wall[self.position[2]-5][self.position[3]]==0 and
        collision.wall[self.position[0]+5][self.position[3]]==0) and self.state!='jump':
            if self.direction=="right":
                self.image = Image.open("./res/character/ch_right_down.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_left_down.png").resize(self.size)
            print("바닥에서 뜸")
            self.position[1] += 3
            self.position[3] += 3

        elif self.state=='jump' and self.count > 8:
            if (collision.wall[self.position[2]-12][self.position[3]]==1 and collision.wall[self.position[0]+5][self.position[3]]) or \
             (collision.wall[self.position[2]-12][self.position[3]]==1 and collision.wall[self.position[2]-5][self.position[3]]):
                print("바닥에서 착지")
                self.state=None
                self.count=0


        #오른쪽 벽 체크
        elif collision.wall[self.position[2]-5][self.position[3]-12]==1 and self.direction=='right':
            self.i+=1
            print(self.position[2],self.position[3])
            print("오른쪽 충돌",self.i)
            self.position[0] -=5 
            self.position[2] -=5
        #왼쪽 벽 체크
        elif collision.wall[self.position[0]+5][self.position[3]-12]==1 and self.direction=='left':
            print(self.position[0],self.position[3])
            self.i+=1
            print("왼쪽 충돌",self.i)
            self.position[0] +=5
            self.position[2] +=5 
        # #바닥 체크