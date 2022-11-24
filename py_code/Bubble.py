from PIL import Image
class Bubble:
    def __init__(self):
        self.size = (15,15)
        self.image = Image.open("./res/bubble.png").resize(self.size)