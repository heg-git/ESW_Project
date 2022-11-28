from Bubble import Bubble

class BubblePool():
    def __init__(self, num):
        self.bubble = []
        for i in range(num):
            self.bubble.append(Bubble())