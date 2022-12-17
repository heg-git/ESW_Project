from Singleton import Singleton
from BubblePool import BubblePool
from Bubble import Bubble

class BubbleManager(Singleton):
    def __init__(self):
        print("버블 매니저 생성")
        self.bubble_pool = BubblePool(15)

    def create_bubble(self):
        print("버블 10개추가생성")
        for i in range(10):
            self.bubble_pool.bubble.append(Bubble())

    def get_bubble(self):
        print("pool에 남은 버블", len(self.bubble_pool.bubble)-1)
        return self.bubble_pool.bubble.pop(0)

    def put_bubble(self, bubble):
        self.bubble_pool.bubble.append(bubble)
        print("pool에 남은 버블", len(self.bubble_pool.bubble))


    def mov_bubble(self, bubble):
        for b in bubble:
            if b.move_count==12:
                b.move_count=0
                self.put_bubble(bubble.pop(0))
            elif b.direction == "right":
                b.position[0] += b.speed
                b.position[2] += b.speed
                b.move_count+=1
            else:
                b.position[0] -= b.speed
                b.position[2] -= b.speed
                b.move_count+=1

    def bubble_hit(self, bubble, enemy):
        for idx, b in enumerate(bubble):
            for en in enemy:
                for bxp in range(b.position[0]+4, b.position[2]-4):
                    for exp in range(en.position[0]+5, en.position[2]-5):
                        for eyp in range(en.position[1]+3, en.position[3]-3):
                            if bxp == exp and b.position[1]+6 == eyp:
                                en.bubbled()
                                self.put_bubble(bubble.pop(idx))
                                return 50
        return 0
                                