from PIL import Image
class Enemy2:
    def __init__(self, idx, position):
        self.state = None
        self.direction = None
        self.size = (20,20)
        self.position = position
        self.move_count = 0
        self.flag = 0
        
        # dicision direction
        if idx%2==0:
            self.image = Image.open("./res/enemy2/en2_right_1.png").resize(self.size)
            self.direction = "right"
        else:
            self.image = Image.open("./res/enemy2/en2_left_1.png").resize(self.size)
            self.direction = "left"

    # make bubble state
    def bubbled(self):
        self.state = "bubbled"
        if self.direction == "right":
            self.image = Image.open("./res/enemy2/en2_right_bubbled.png").resize(self.size)
        else:
            self.image = Image.open("./res/enemy2/en2_left_bubbled.png").resize(self.size)