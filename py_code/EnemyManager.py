from Enemy import Enemy
from PIL import Image
import random

class EnemyManager:
    def __init__(self, num):
        self.enemy = []
        
        for i in range(num):
            self.enemy.append(Enemy(), )

    def move(self):
        if self.state=='bubbled':
            return 
        if self.move_count<15:
            self.flag = 0 if self.flag else 1
            if self.flag:
                self.image = Image.open("./res/enemy/en_left_1.png").resize(self.size)
            else:
                self.image = Image.open("./res/enemy/en_left_2.png").resize(self.size)
            self.position[0] -= self.speed
            self.position[2] -= self.speed
            self.move_count+=1
            self.direction = "left"
                
        elif self.move_count<30:
            self.flag = 0 if self.flag else 1
            if self.flag:
                self.image = Image.open("./res/enemy/en_right_1.png").resize(self.size)
            else:
                self.image = Image.open("./res/enemy/en_right_2.png").resize(self.size)
            self.position[0] += self.speed
            self.position[2] += self.speed
            self.move_count+=1
            self.direction = "right"
        else:
            self.move_count=0

    def bubbled(self):
        self.state = "bubbled"
        self.image = Image.open("./res/enemy/en_right_bubbled.png").resize(self.size)