from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb

from Character import Character
from Enemy import Enemy
from Joystick import Joystick
from BubbleManager import BubbleManager
from Bubble import Bubble

def main():
    joystick = Joystick()
    character = Character()
    enemy = []
    enemy_position=[[205, 215, 225, 235],[170, 177, 190, 197],[170, 138, 190, 158],[170, 102, 190, 122]]
    for i in range(4):
        enemy.append(Enemy(enemy_position[i]))
    map = Image.open("./res/etc/map.png").resize((240,240))
    pressed=False
    while True:
        my_map=map.copy()
        
    # if not joystick.button_U.value:  # up pressed
    #     character.move('up')

    # if not joystick.button_D.value:  # down pressed
    #     character.move('down')

        if not joystick.button_L.value:  # left pressed
            character.move('left')

        if not joystick.button_R.value:  
            character.move('right')

        if not joystick.button_B.value:
            character.state = 'jump'

        if not joystick.button_A.value:
            pressed=True
        elif joystick.button_A.value and pressed:
            print("attack 눌렀다 뗌")
            character.attack()
            pressed=False

        if character.state == 'jump':
            character.jump()

        character.mov_bubble()


        for en in enemy:
            my_map.paste(en.image, en.position, en.image)
            en.move()

        for bubble in character.bubble:
            my_map.paste(bubble.image, bubble.position, bubble.image)
        character.mov_bubble()
        my_map.paste(character.image, character.position, character.image)
        joystick.disp.image(my_map)
        
if __name__ == '__main__':
    main()