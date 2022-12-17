import numpy as np
from PIL import Image, ImageDraw
from BubbleManager import BubbleManager

class Character:
    def __init__(self):
        self.state = None
        self.position = np.array([30, 210, 53, 233])
        self.size = (23, 23)
        self.image = Image.open("./res/character/ch_right_1.png").resize(self.size)
        self.flag = 0
        self.count = 0
        self.direction = "right"
        self.gravity = 4
        self.life = 3
        self.life_image = Image.open("./res/etc/life.png").resize((10,10))
        self.bubble_manager = BubbleManager()
        self.bubble = []
        self.speed = 4
        self.air = False

    def move(self, command):
        if command == "left":
            self.direction = "left"
            self.flag = 0 if self.flag else 1
            if self.flag:
                self.image = Image.open("./res/character/ch_left_1.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_left_2.png").resize(self.size)
            self.position[0] -= self.speed
            self.position[2] -= self.speed
                
        elif command == "right":
            self.direction = "right"
            self.flag = 0 if self.flag else 1
            if self.flag:
                self.image = Image.open("./res/character/ch_right_1.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_right_2.png").resize(self.size)
            self.position[0] += self.speed
            self.position[2] += self.speed
        
        # elif command == "up":
        #     self.direction = "left"
        #     self.flag = 0 if self.flag else 1
        #     if self.flag:
        #         self.image = Image.open("./res/character/ch_left_1.png").resize(self.size)
        #     else:
        #         self.image = Image.open("./res/character/ch_left_2.png").resize(self.size)
        #     self.position[1] -= 5
        #     self.position[3] -= 5

    def jump(self):
        if self.air:
            self.state = None
            return
        if self.count < 10:
            if self.direction=="right":
                self.image = Image.open("./res/character/ch_right_jump.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_left_jump.png").resize(self.size)
            
            self.position[1] -= self.gravity
            self.position[3] -= self.gravity
            #self.gravity -= 1
            self.count += 1

        elif self.count < 20:
            self.state = 'fall'
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
            self.count = 0
            self.state = None
        
    def attack(self):
        if len(self.bubble_manager.bubble_pool.bubble)==0:
            self.bubble_manager.create_bubble()
        else:
            self.bubble.append(self.bubble_manager.get_bubble())

        if self.direction=="right":
            self.image = Image.open("./res/character/ch_right_attack.png").resize(self.size)
            self.bubble[-1].position = np.array([self.position[2], self.position[1]+3, self.position[2]+15, self.position[1]+18])
            self.bubble[-1].direction = "right"
        else:
            self.image = Image.open("./res/character/ch_left_attack.png").resize(self.size)
            self.bubble[-1].direction = "left"
            self.bubble[-1].position = np.array([self.position[0]-15, self.position[1]+3, self.position[0], self.position[1]+18])
            


    def mov_bubble(self):
        self.bubble_manager.mov_bubble(self.bubble)

    def colision_check(self, collision):

        if ((collision.wall[self.position[0]+12][self.position[3]]==1 and collision.wall[self.position[0]+5][self.position[3]]) or \
            (collision.wall[self.position[0]+12][self.position[3]]==1 and collision.wall[self.position[2]-5][self.position[3]])) and self.state!='jump':
            self.state=None
            self.air=False
            self.count=0

        #오른쪽 벽 체크
        for i in range(225,240):
            if self.position[2]-5 == i:
                print("오른쪽 충돌")
                self.position[0] -=4
                self.position[2] -=4
                self.ground_check(collision)
        

        #왼쪽 벽 체크
        for i in range(17):
            if self.position[0]+5 == i:
                print("왼쪽 충돌")
                self.position[0] +=4
                self.position[2] +=4
                self.ground_check(collision)
        

    def ground_check(self, collision):
        if self.state=='jump':
            return

        if(collision.wall[self.position[2]-5][self.position[3]]==0 and
            collision.wall[self.position[0]+5][self.position[3]]==0):
                if self.state=='fall':
                    return
                if self.direction=="right":
                    self.image = Image.open("./res/character/ch_right_down.png").resize(self.size)
                else:
                    self.image = Image.open("./res/character/ch_left_down.png").resize(self.size)
                print("공중에 뜸")
                self.position[1] += 3
                self.position[3] += 3
                self.air=True
                              
    def bubble_hit(self, enemy):
        return self.bubble_manager.bubble_hit(self.bubble, enemy)

    def enemy_hit(self, enemy):
        for idx, en in enumerate(enemy):
            for cxp in range(self.position[0]+5, self.position[2]-5):
                for exp in range(en.position[0]+5, en.position[2]-5):
                    for eyp in range(en.position[1]+5, en.position[3]-5):
                        if cxp == exp and self.position[1]+12==eyp:
                            if en.state == 'bubbled':
                                return idx
                            return -1
        return -2

    def respawn(self):
        self.image = Image.open("./res/character/ch_right_1.png").resize(self.size)
        self.state = None
        self.position = [30, 210, 53, 233]