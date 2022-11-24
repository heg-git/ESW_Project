import numpy as np
from PIL import Image, ImageDraw

class Character:
    def __init__(self):
        self.appearance = "character"
        self.state = None
        self.position = [15, 210, 40, 235]
        self.size = (25,25)
        self.image = Image.open("./res/ch_1_right.png").resize(self.size)
        self.flag = 0
        self.count = 0
        self.direction = "right"
        self.gravity=9

    def move(self, command):
    #     if command == "up":
    #         self.position[1] -= 5
    #         self.position[3] -= 5

    #     elif command == "down":
    #         self.position[1] += 5
    #         self.position[3] += 5

        if command == "left":
            self.direction = "left"
            self.flag = 0 if self.flag else 1
            if self.flag:
                self.image = Image.open("./res/ch_1_left.png").resize(self.size)
            else:
                self.image = Image.open("./res/ch_2_left.png").resize(self.size)
            self.position[0] -= 5
            self.position[2] -= 5
                
        elif command == "right":
            self.direction = "right"
            self.flag = 0 if self.flag else 1
            if self.flag:
                self.image = Image.open("./res/ch_1_right.png").resize(self.size)
            else:
                self.image = Image.open("./res/ch_2_right.png").resize(self.size)
            self.position[0] += 5
            self.position[2] += 5

    def jump(self):
        if self.count < 8:
            if self.direction=="right":
                self.image = Image.open("./res/ch_r_j.png").resize(self.size)
            else:
                self.image = Image.open("./res/ch_l_j.png").resize(self.size)
            
            self.position[1] -= self.gravity
            self.position[3] -= self.gravity
            self.gravity -= 1
            self.count += 1


        elif self.count < 16:
            if self.direction=="right":
                self.image = Image.open("./res/ch_r_d.png").resize(self.size)
            else:
                self.image = Image.open("./res/ch_l_d.png").resize(self.size)
            
            self.gravity += 1
            self.position[1] += self.gravity
            self.position[3] += self.gravity
            self.count+=1

        else:
            if self.direction=="right":
                self.image = Image.open("./res/ch_1_right.png").resize(self.size)
            else:
                self.image = Image.open("./res/ch_1_left.png").resize(self.size)
            self.count=0
            self.state = None
        
    def attack(self):
        if self.direction=="right":
                self.image = Image.open("./res/ch_a_r.png").resize(self.size)
        else:
            self.image = Image.open("./res/ch_a_l.png").resize(self.size)