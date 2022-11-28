from PIL import Image
class Bubble:
    def __init__(self):
        self.size = (15,15)
        self.image = Image.open("./res/etc/bubble.png").resize(self.size)
        self.position = [0,0,15,15]
        self.direction = "right"
        self.move_count = 0