from PIL import Image
class Enemy1:
    def __init__(self, idx, position, distance):
        self.state = None
        self.size = (20,20)
        self.position = position
        self.move_count = 0
        self.flag = 1
        self.distance = int(distance/2)
        self.jump = True
        self.jump_count = 0

        if idx%2==0:
            self.direction = "left"
            self.image = Image.open("./res/enemy1/en_left_1.png").resize(self.size)
        else:
            self.direction = "right"
            self.image = Image.open("./res/enemy1/en_right_1.png").resize(self.size)
            self.move_count = self.distance

    def bubbled(self):
        self.state = "bubbled"
        if self.direction == "right":
            self.image = Image.open("./res/enemy1/en_right_bubbled.png").resize(self.size)
        else:
            self.image = Image.open("./res/enemy1/en_left_bubbled.png").resize(self.size)