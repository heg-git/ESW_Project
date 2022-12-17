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
    enemy_position=np.array([[140, 213, 160, 233],[170, 177, 190, 197],[170, 140, 190, 160],[170, 100, 190, 120]])
    score = 0
    for i in range(4):
        enemy.append(Enemy(enemy_position[i]))
        #enemy[-1].bubbled()
    map = Image.open("./res/etc/map3.png").resize((240,240))
    collision=MapCollision()
    pressed=False

    my_draw=ImageDraw.Draw(map)
    # #왼쪽 기둥
    # my_draw.rectangle((0,20,16,240), fill=(255, 255, 255, 100))
    # #땅
    # my_draw.rectangle((0,233,240,240), fill=(255, 255, 255, 100))
    # #오른쪽 기둥
    # my_draw.rectangle((225,20,240,240), fill=(255, 255, 255, 100))
    
    # #오른쪽 발판1
    # my_draw.rectangle((138,196,200,201), fill=(255, 255, 255, 100))
    # #오른쪽 발판2
    # my_draw.rectangle((138,149,200,155), fill=(255, 255, 255, 100))
    # #오른쪽 발판3
    # my_draw.rectangle((138,99,200,104), fill=(255, 255, 255, 100))

    # #왼쪽 발판1
    # my_draw.rectangle((38,175,101,180), fill=(255, 255, 255, 100))
    # #왼쪽 발판2
    # my_draw.rectangle((38,123,101,128), fill=(255, 255, 255, 100))
    # #왼쪽 발판3
    # my_draw.rectangle((38,73,101,78), fill=(255, 255, 255, 100))

    joystick.disp.image(map)
    my_draw.text((25, 2), "LIFE", font=fnt, fill=(0,255,0))
    rectangle = ImageDraw.Draw(map)

    while True:
        rectangle.rectangle((110, 2, 220, 15), fill=(255,255,255))
        rectangle.text((110, 2),("HIGH SCORE: "+str(score)),font=fnt2, fill=(255,0,0))
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
            character.attack()
            score += 10
            pressed=False

        character.mov_bubble()

        if character.state == 'jump' or character.state == 'fall':
                character.jump()

        for en in enemy:
            my_map.paste(en.image, en.position, en.image)
            en.move()

        for bubble in character.bubble:
            my_map.paste(bubble.image, bubble.position, bubble.image)
        
        character.ground_check(collision)
        character.colision_check(collision)
        result=character.enemy_hit(enemy)
        if result == None:
            pass
        elif result == -1:
            print("죽음")
            character.life -= 1
            score -= 50
            character.respawn()
        else:
            print(result, "번 째 적 죽음")
            enemy.pop(result)

        character.bubble_hit(enemy)
        
        for life in range(character.life):
            my_map.paste(character.life_image, (60+(life*10), 5 ,70+(life*10) , 15 ), character.life_image)

        if character.life < 0 :
            break

        my_map.paste(character.image, character.position, character.image)


        joystick.disp.image(my_map)
        
if __name__ == '__main__':
    main()