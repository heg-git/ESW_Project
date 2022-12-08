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
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
    fnt2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    joystick = Joystick()
    character = Character()
    enemy = []
    enemy_position=[[204, 215, 225, 236],[171, 177, 192, 198],[171, 138, 192, 159],[171, 102, 192, 123]]

    for i in range(4):
        enemy.append(Enemy(enemy_position[i]))
    map = Image.open("./res/etc/map2.png").resize((240,240))
    collision=MapCollision()
    pressed=False

    my_draw=ImageDraw.Draw(map)
    #왼쪽 기둥
    my_draw.rectangle((0,20,16,240), fill=(255, 255, 255, 100))
    #땅
    my_draw.rectangle((0,233,240,240), fill=(255, 255, 255, 100))
    #오른쪽 기둥
    my_draw.rectangle((225,20,240,240), fill=(255, 255, 255, 100))
    
    #오른쪽 발판1
    my_draw.rectangle((138,200,200,208), fill=(255, 255, 255, 100))
    #오른쪽 발판2
    my_draw.rectangle((138,161,200,171), fill=(255, 255, 255, 100))
    #오른쪽 발판3
    my_draw.rectangle((138,117,200,127), fill=(255, 255, 255, 100))
    #오른쪽 발판4
    my_draw.rectangle((138,78,200,88), fill=(255, 255, 255, 100))
    
    #왼쪽 발판1
    my_draw.rectangle((38,182,101,192), fill=(255, 255, 255, 100))
    #왼쪽 발판2
    my_draw.rectangle((38,138,101,148), fill=(255, 255, 255, 100))
    #왼쪽 발판3
    my_draw.rectangle((38,94,101,104), fill=(255, 255, 255, 100))

    joystick.disp.image(map)
    my_draw.text((25, 2), "LIFE", font=fnt, fill=(0,255,0))
    my_draw.text((110, 2), ("HIGH SCORE   "+str(10)),font=fnt2, fill=(255,0,0))

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
            character.attack()
            pressed=False

        character.mov_bubble()

        for en in enemy:
            my_map.paste(en.image, en.position, en.image)
            en.move()

        for bubble in character.bubble:
            my_map.paste(bubble.image, bubble.position, bubble.image)

        for life in range(character.life):
            my_map.paste(character.life_image, (60+(life*10), 5 ,70+(life*10) , 15 ), character.life_image)
        
        character.ground_check(collision)

        if character.state == 'jump' or character.state == 'fall':
                print(character.state)
                character.jump()
                    
        character.colision_check(collision)

        character.hit_check(enemy)

        my_map.paste(character.image, character.position, character.image)
        joystick.disp.image(my_map)
        
if __name__ == '__main__':
    main()