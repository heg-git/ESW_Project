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
    fnt1 = ImageFont.truetype("./res/etc/DungGeunMo.ttf", 20)
    fnt2 = ImageFont.truetype("./res/etc/DungGeunMo.ttf", 20)
    fnt3 = ImageFont.truetype("./res/etc/DungGeunMo.ttf", 15)
    fnt4 = ImageFont.truetype("./res/etc/DungGeunMo.ttf", 16)
    
    joystick = Joystick()
    character = Character()
    enemy = []
    enemy_position=np.array([[140, 213, 160, 233],[170, 177, 190, 197],[170, 140, 190, 160],[170, 100, 190, 120]])
    score = 0
    for i in range(4):
        enemy.append(Enemy(enemy_position[i]))
        #enemy[-1].bubbled()
    map = Image.open("./res/etc/map3.png").resize((240,240))
    game_clear = Image.open("./res/etc/game_clear.png").resize((240,240))
    game_over = Image.open("./res/etc/game_over.png").resize((240,240))
    collision=MapCollision()
    pressed=False
    start=0
    start = Image.open("./res/etc/start.png").resize((240,240))

    ImageDraw.Draw(start).text((60, 180), "ESW PROJECT", font=fnt1, fill=(255,0 ,0))
    ImageDraw.Draw(start).text((27, 205),("PRESS A TO START!!") ,font=fnt2, fill=(255,255,255))

    joystick.disp.image(start)
    while True:  
        if not joystick.button_A.value:
            pressed=True
        elif joystick.button_A.value and pressed:
            pressed=False
            break
    
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

    #joystick.disp.image(map)
    ImageDraw.Draw(map).text((25, 2), "LIFE", font=fnt3, fill=(0,255,0))
    ImageDraw.Draw(map).text((105, 2),("HIGH SCORE "),font=fnt4, fill=(255,0,0))
    while True:
        my_map=map.copy()
        ImageDraw.Draw(my_map).text((190, 2), str(score),font=fnt4)
        
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
            score += 5
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

        if result == -2:
            pass
        elif result == -1:
            character.life -= 1
            score -= 100
            character.respawn()
        else:
            score += 300
            enemy.pop(result)

        score += character.bubble_hit(enemy)
        
        for life in range(character.life):
            my_map.paste(character.life_image, (60+(life*10), 5 ,70+(life*10) , 15 ), character.life_image)

        my_map.paste(character.image, character.position, character.image)

        if len(enemy)==0:
            joystick.disp.image(game_clear)
            break
        
        if character.life < 0 :
            joystick.disp.image(game_over)
            break

        joystick.disp.image(my_map)
        
if __name__ == '__main__':
    main()