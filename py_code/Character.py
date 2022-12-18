import numpy as np
from PIL import Image
from BubbleManager import BubbleManager

class Character:
    def __init__(self):

        #define character information
        self.state = None
        self.position = np.array([15, 210, 38, 233])
        self.size = (23, 23)
        self.image = Image.open("./res/character/ch_right_1.png").resize(self.size)
        self.flag = 0
        self.direction = "right"
        self.jump_count = 0
        self.gravity = 4
        self.speed = 5
        self.life = 3
        self.life_image = Image.open("./res/etc/life.png").resize((10,10))
        self.air = False
        self.bubble_manager = BubbleManager()
        self.bubble = []

    #move character according to direction
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

    #jump character according to direction
    def jump(self):
        #can't jump if character floating in the air
        if self.air:
            self.state = None
            return
        #go up 10 time
        if self.jump_count < 10:
            if self.direction=="right":
                self.image = Image.open("./res/character/ch_right_jump.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_left_jump.png").resize(self.size)
            
            self.position[1] -= self.gravity
            self.position[3] -= self.gravity
            self.jump_count += 1
        
        #fall down 10 time
        elif self.jump_count < 20:
            self.state = 'fall'
            if self.direction=="right":
                self.image = Image.open("./res/character/ch_right_down.png").resize(self.size)
            else:
                self.image = Image.open("./res/character/ch_left_down.png").resize(self.size)

            self.position[1] += self.gravity
            self.position[3] += self.gravity
            self.jump_count+=1
        
        #else init state none
        else:
            self.jump_count = 0
            self.state = None

    #shoot bubble
    def attack(self):
        #create bubble if all bubble used
        if len(self.bubble_manager.bubble_pool.bubble)==0:
            self.bubble_manager.create_bubble()
        #else get bubble from bubble manager
        else:
            self.bubble.append(self.bubble_manager.get_bubble())

        #shoot bubble according to direction
        if self.direction=="right":
            self.image = Image.open("./res/character/ch_right_attack.png").resize(self.size)
            self.bubble[-1].position = np.array([self.position[2], self.position[1]+3, self.position[2]+15, self.position[1]+18])
            self.bubble[-1].direction = "right"
        else:
            self.image = Image.open("./res/character/ch_left_attack.png").resize(self.size)
            self.bubble[-1].direction = "left"
            self.bubble[-1].position = np.array([self.position[0]-15, self.position[1]+3, self.position[0], self.position[1]+18])
            
    #move all bubble from bubble manager
    def mov_bubble(self):
        self.bubble_manager.mov_bubble(self.bubble)

    def colision_check(self, collision):

        #check if character is on ground (not check when state is jump)
        if ((collision.wall[self.position[0]+12][self.position[3]]==1 and collision.wall[self.position[0]+5][self.position[3]]) or \
            (collision.wall[self.position[0]+12][self.position[3]]==1 and collision.wall[self.position[2]-5][self.position[3]])) and self.state!='jump':
            self.state=None
            self.air=False
            self.jump_count=0

        #check right wall
        for i in range(225,240):
            if self.position[2]-5 == i:
                self.position[0] -= 5
                self.position[2] -= 5
                self.ground_check(collision)
        
        #check left wall
        for i in range(17):
            if self.position[0]+5 == i:
                self.position[0] += 5
                self.position[2] += 5
                self.ground_check(collision)
    
    #check if character is floating in the air
    def ground_check(self, collision):
        #pass if jump state
        if self.state=="jump" or self.state=="fall":
            return
        #compare character position with map collision 
        if(collision.wall[self.position[2]-5][self.position[3]]==0 and
            collision.wall[self.position[0]+5][self.position[3]]==0):
                if self.direction=="right":
                    self.image = Image.open("./res/character/ch_right_down.png").resize(self.size)
                else:
                    self.image = Image.open("./res/character/ch_left_down.png").resize(self.size)

                self.position[1] += 3
                self.position[3] += 3
                self.air=True
                              
    #check bubble hit from bubble manager
    def bubble_hit(self, enemy):
        return self.bubble_manager.bubble_hit(self.bubble, enemy)

    #check character <-> enemy collision
    def enemy_hit(self, enemy):
        for idx, en in enumerate(enemy):
            for ch_x in range(self.position[0]+5, self.position[2]-5):
                for en_x in range(en.position[0]+5, en.position[2]-5):
                    for en_y in range(en.position[1]+5, en.position[3]-5):
                        if ch_x == en_x and self.position[1]+12==en_y:
                            if en.state == 'bubbled':
                                return idx
                            return -1
        return -2

    #respawn character
    def respawn(self):
        self.image = Image.open("./res/character/ch_right_1.png").resize(self.size)
        self.state = None
        self.position = [15, 210, 38, 233]