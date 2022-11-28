import numpy as np
from PIL import Image, ImageDraw
from BubbleManager import BubbleManager

class Character:
    def __init__(self):
        self.appearance = "character"
        self.state = None
        self.position = [15, 210, 40, 235]
        self.size = (25,25)
        self.image = Image.open("./res/character/ch_right_1.png").resize(self.size)
        self.flag = 0
        self.count = 0
        self.direction = "right"
        self.gravity = 9

        self.bubble_manager = BubbleManager()
        self.bubble=[]

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

    def jump(self):
        if self.count < 8:
            if self.direction=="right":
                self.image = Image.open("./res/character/ch_right_jump.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_left_jump.png").resize(self.size)
            
            self.position[1] -= self.gravity
            self.position[3] -= self.gravity
            self.gravity -= 1
            self.count += 1


        elif self.count < 16:
            if self.direction=="right":
                self.image = Image.open("./res/character/ch_right_down.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_left_down.png").resize(self.size)
            
            self.gravity += 1
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
                
        else:
            self.image = Image.open("./res/character/ch_left_attack.png").resize(self.size)
            self.bubble[-1].position = [self.position[0]-15, self.position[1]+3, self.position[0], self.position[1]+18]
            self.bubble[-1].direction = "left"


    def mov_bubble(self):
        self.bubble_manager.mov_bubble(self.bubble)
