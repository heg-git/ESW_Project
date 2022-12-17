from PIL import Image
import numpy as np
class Bubble:
    def __init__(self):
        self.size = (15,15)
        self.image = Image.open("./res/etc/bubble.png").resize(self.size)
        self.position = np.zeros(4)
        self.speed = 2
        self.direction = "right"
        self.move_count = 0
    