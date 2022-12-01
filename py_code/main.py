from PIL import Image, ImageDraw, ImageFont
import numpy as np
import time
import random
from colorsys import hsv_to_rgb

from Character import Character
from Enemy import Enemy
from MapCollision import MapCollision
from Joystick import Joystick

def main():
    joystick = Joystick()
    character = Character()
    enemy = []
    enemy_position=[[205, 215, 225, 235],[170, 177, 190, 197],[170, 138, 190, 158],[170, 102, 190, 122]]
    for i in range(4):
        enemy.append(Enemy(enemy_position[i]))
    map = Image.open("./res/etc/map.png").resize((240,240))
    collision=MapCollision()
    pressed=False

    my_draw=ImageDraw.Draw(map)
    # #왼쪽
    # my_draw.rectangle((0,20,16,240), fill=(255, 255, 255, 100))
    # #땅
    #my_draw.rectangle((0,233,240,240), fill=(255, 255, 255, 100))
    # #오른쪽
    # my_draw.rectangle((225,20,240,240), fill=(255, 255, 255, 100))
    # #가운데1
    #my_draw.rectangle((60,195,186,200), fill=(255, 255, 255, 100))
    joystick.disp.image(map)

    while True:
        my_map=map.copy()
        
        if not joystick.button_U.value:  # up pressed
            character.move('up')

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

        if character.state == 'jump' :
            character.jump()

        character.mov_bubble()
        character.colision_check(collision)

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