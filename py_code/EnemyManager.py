from Enemy1 import Enemy1
from Enemy2 import Enemy2
from PIL import Image
import random
import numpy as np
class EnemyManager:
    def __init__(self, en1, en2):
        self.en1 = en1
        self.en2 = en2
        self.enemy = []
        #self.enemy2 = []
        self.enemy1_position=np.array([[200, 213, 220, 233],[40, 155, 60, 175], [180, 127, 200, 147],[40, 50, 60, 70]])
        self.enemy2_position=np.array([[15, 60, 35, 80],[190, 60, 210, 80]])
        self.create_enemy(self.en1, self.en2)
        #self.create_enemy2(en2)

    def create_enemy(self, en1, en2):
        for i in range(en1):
            self.enemy.append(Enemy1(i, self.enemy1_position[i], 54))
        
        for i in range(en2):
            self.enemy.append(Enemy2(i, self.enemy2_position[i]))
    # def create_enemy2(self, num):
    #     for i in range(num):
    #         self.enemy2.append(Enemy2(i, self.enemy2_position[i]))

    
    def move(self, character_position):
        
        for en in self.enemy[:self.en1]:
            
            speed = random.randrange(4,8)

            if en.state == "bubbled":
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

        
        for en in self.enemy[self.en1:]:
    
            speed = 2

            if en.state == "bubbled":
                continue
            ch_x = int((character_position[0]+character_position[2])/2)
            ch_y = int((character_position[1]+character_position[3])/2)
            
            en_x = int((en.position[0]+en.position[2])/2)
            en_y = int((en.position[1]+en.position[3])/2)

            if en_x < ch_x:
                if en.flag < 4:
                    en.image = Image.open("./res/enemy2/en2_right_1.png").resize(en.size)
                
                elif en.flag <8:
                    en.image = Image.open("./res/enemy2/en2_right_2.png").resize(en.size)
                else:
                    en.flag=0
                en.position[0] += speed
                en.position[2] += speed

            elif en_x > ch_x:
                if en.flag < 4:
                    en.image = Image.open("./res/enemy2/en2_left_1.png").resize(en.size)
                elif en.flag <8:
                    en.image = Image.open("./res/enemy2/en2_left_2.png").resize(en.size)
                else:
                    en.flag=0
                en.position[0] -= speed
                en.position[2] -= speed
            
            if en_y < ch_y:
                en.position[1] += speed
                en.position[3] += speed

            elif en_y > ch_y:
                en.position[1] -= speed
                en.position[3] -= speed
            
            en.flag+=1


    def paste(self, map):
        for en in self.enemy:
            map.paste(en.image, en.position, en.image)
        
    def ground_check(self, collision):
        for en in self.enemy[:self.en1]:
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
        for en in self.enemy[:self.en1]:
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
