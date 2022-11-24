from Singleton import Singleton
from BubblePool import BubblePool
from Bubble import Bubble

class BubbleManager(Singleton):
    def __init__(self):
        print("버블 매니저 생성")
        self.bubble_pool = BubblePool(20)
    
    def mov_bubble(self, bubble):
        for b in bubble:
            if b.move_count==20:
                self.bubble_pool.put_object(bubble.pop(0))
                print("bubble 소멸")
            elif b.direction == "right":
                b.position[0] +=3
                b.position[2] +=3
                b.move_count+=1
            else:
                b.position[0] -=3
                b.position[2] -=3
                b.move_count+=1