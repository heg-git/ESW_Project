from PIL import Image
class Enemy:
    def __init__(self, position):
        self.size = (20,20)
        self.image = Image.open("./res/enemy/en_left_1.png").resize(self.size)
        self.position = position
        self.direction = "left"
        self.move_count = 0
        self.flag = 1

    def move(self):
        if self.move_count<10:
            self.flag = 0 if self.flag else 1
            if self.flag:
                self.image = Image.open("./res/enemy/en_left_1.png").resize(self.size)
            else:
                self.image = Image.open("./res/enemy/en_left_2.png").resize(self.size)
            self.position[0] -= 5
            self.position[2] -= 5
            self.move_count+=1
                
        elif self.move_count<20:
            self.flag = 0 if self.flag else 1
            if self.flag:
                self.image = Image.open("./res/enemy/en_right_1.png").resize(self.size)
            else:
                self.image = Image.open("./res/enemy/en_right_2.png").resize(self.size)
            self.position[0] += 5
            self.position[2] += 5
            self.move_count+=1
        
        else:
            self.move_count=0