from Singleton import Singleton
from BubbleManager import BubbleManager

print('1번째 생성')
s1 = BubbleManager()# create
print('2번째 생성')
s2 = BubbleManager() # recycle
print('s1 == s2')
print(s1==s2) # true