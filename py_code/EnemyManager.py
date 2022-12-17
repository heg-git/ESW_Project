from Enemy1 import Enemy1
from PIL import Image
import random
import numpy as np
class EnemyManager:
    def __init__(self):
        self.enemy1 = []
        self.enemy2 = []
        self.position=np.array([[200, 213, 220, 233],[40, 155, 60, 175], [180, 127, 200, 147],[40, 50, 60, 70]])
        self.create_enemy1(4)

    def create_enemy1(self, num):
        for i in range(num):
            self.enemy1.append(Enemy1(i, self.position[i], 54))

    
    def move(self):
        for en in self.enemy1:
            speed = random.randrange(4,8)

            if en.state=="bubbled":
                    continue
            
            if en.move_count < en.distance:
                en.flag = 0 if en.flag else 1
                if en.flag:
                    en.image = Image.open("./res/enemy1/en_left_1.png").resize(en.size)
                else:
                    en.image = Image.open("./res/enemy1/en_left_2.png").resize(en.size)
                en.position[0] -= speed
                en.position[2] -= speed
                en.move_count+=1
                en.direction = "left"
                    
            elif en.move_count < 2*en.distance:
                en.flag = 0 if en.flag else 1
                if en.flag:
                    en.image = Image.open("./res/enemy1/en_right_1.png").resize(en.size)
                else:
                    en.image = Image.open("./res/enemy1/en_right_2.png").resize(en.size)
                en.position[0] += speed
                en.position[2] += speed
                en.move_count+=1
                en.direction = "right"
            
            else:
                en.move_count=0

    def paste(self, map):
        for en in self.enemy1:
            map.paste(en.image, en.position, en.image)

    def ground_check(self, collision):
        for en in self.enemy1:
            if(collision.wall[en.position[2]-5][en.position[3]]==0 and
                collision.wall[en.position[0]+5][en.position[3]]==0) and not en.jump:
                    if en.state != "bubbled":
                        en.state = "fall"
                    en.position[1] += 4
                    en.position[3] += 4
            elif en.state != "bubbled":
                en.state = None

            for i in range(225, 236):
                if en.position[2] == i:
                    en.position[0] -= 5
                    en.position[2] -= 5
                    
            for i in range(10, 17):
                if en.position[0] == i:
                    en.position[0] += 5
                    en.position[2] += 5
                    
    def jump(self):
        for en in self.enemy1:
            if en.state=="bubbled" or en.position[1]<30:
                en.jump=False
                continue
            num = random.randrange(0, 15)
            if num==0 and en.state != "fall":
                en.jump=True
            if en.jump:
                if en.jump_count>8:
                    en.jump_count=0
                    en.jump=False
                    continue
                en.position[1] -= 4
                en.position[3] -= 4
                en.jump_count += 1
