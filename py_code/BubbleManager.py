from Singleton import Singleton
from BubblePool import BubblePool
from Bubble import Bubble

class BubbleManager(Singleton):
    def __init__(self):
        print("버블 매니저 생성")
        self.bubble_pool = BubblePool(20)
    
    def mov_bubble(self, bubble):
        for b in bubble:
            if b.direction == "right":
                b.position[0] +=5
                b.position[2] +=5
            else:
                b.position[0] -=5
                b.position[2] -=5