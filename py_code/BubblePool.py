from ObjectPool import ObjectPool
from Bubble import Bubble

class BubblePool(ObjectPool):
    def __init__(self, num):
        self.bubble = []
        for i in range(num):
            self.bubble.append(Bubble())

    def create_object(self):
        print("버블 10개추가생성")
        for i in range(10):
            self.bubble.append(Bubble())

    def get_object(self):
        print("pool에 남은 버블", len(self.bubble)-1)
        return self.bubble.pop(0)

    def put_object(self, bubble):
        print("pool에 남은 버블", len(self.bubble)-1)
        self.bubble.append(bubble)