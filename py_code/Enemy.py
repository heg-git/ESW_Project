from PIL import Image
class Enemy:
    def __init__(self, position):
        self.state = None
        self.size = (21,21)
        self.image = Image.open("./res/enemy/en_left_1.png").resize(self.size)
        self.position = position
        self.direction = "left"
        self.move_count = 0
        self.flag = 1
        self.speed = 3

    def move(self):
        if self.state=='bubbled':
            return 
        if self.move_count<12:
            self.flag = 0 if self.flag else 1
            if self.flag:
                self.image = Image.open("./res/enemy/en_left_1.png").resize(self.size)
            else:
                self.image = Image.open("./res/enemy/en_left_2.png").resize(self.size)
            self.position[0] -= self.speed
            self.position[2] -= self.speed
            self.move_count+=1
            self.direction = "left"
                
        elif self.move_count<24:
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
        self.state='bubbled'
        self.image = Image.open("./res/enemy/en_right_bubbled.png").resize(self.size)