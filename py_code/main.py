from PIL import Image, ImageDraw, ImageFont
import numpy as np
import time
import random
from colorsys import hsv_to_rgb
from Character import Character
from Enemy import Enemy
from MapCollision import MapCollision
from Joystick import Joystick
from EnemyManager import EnemyManager

def main():
    fnt1 = ImageFont.truetype("./res/etc/DungGeunMo.ttf", 20)
    fnt2 = ImageFont.truetype("./res/etc/DungGeunMo.ttf", 20)
    fnt3 = ImageFont.truetype("./res/etc/DungGeunMo.ttf", 15)
    fnt4 = ImageFont.truetype("./res/etc/DungGeunMo.ttf", 16)
    
    joystick = Joystick()
    character = Character()
    enemy_manager = EnemyManager()
    score = 0

    map = Image.open("./res/etc/map1.png").resize((240,240))
    game_clear = Image.open("./res/etc/game_clear.png").resize((240,240))
    game_over = Image.open("./res/etc/game_over.png").resize((240,240))
    collision = MapCollision()
    pressed = False
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
    #map.rectangle((38,30,101,25), fill=(255, 255, 255, 100))

    ImageDraw.Draw(map).text((25, 2), "LIFE", font=fnt3, fill=(0,255,0))
    ImageDraw.Draw(map).text((105, 2),("HIGH SCORE "),font=fnt4, fill=(255,0,0))
    
    #stage 1
    while True:
        my_map=map.copy()
        ImageDraw.Draw(my_map).text((190, 2), str(score),font=fnt4)
        #ImageDraw.Draw(my_map).rectangle((0,30,240,40), fill=(255, 255, 255, 100))

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

        enemy_manager.paste(my_map)
        enemy_manager.move()
        enemy_manager.ground_check(collision)
        enemy_manager.jump()

        for bubble in character.bubble:
            my_map.paste(bubble.image, bubble.position, bubble.image)
        
        character.ground_check(collision)
        character.colision_check(collision)
        result=character.enemy_hit(enemy_manager.enemy)

        if result == -2:
            pass
        elif result == -1:
            character.life -= 1
            score -= 100
            character.respawn()
        else:
            score += 300
            enemy_manager.enemy.pop(result)

        score += character.bubble_hit(enemy_manager.enemy)
        
        for life in range(character.life):
            my_map.paste(character.life_image, (60+(life*10), 5 ,70+(life*10) , 15 ), character.life_image)

        my_map.paste(character.image, character.position, character.image)

        if len(enemy_manager.enemy)==0:
            joystick.disp.image(game_clear)
            break

        if character.life < 0 :
            joystick.disp.image(game_over)
            exit(0)

        joystick.disp.image(my_map)
    print("여기 실행")

    map = Image.open("./res/etc/map1.png").resize((240,240))
    
    #stage 2
    while True:
        print("여기 실행2")
        my_map=map.copy()
        ImageDraw.Draw(my_map).text((190, 2), str(score),font=fnt4)
        #ImageDraw.Draw(my_map).rectangle((0,30,240,40), fill=(255, 255, 255, 100))

        if not joystick.button_L.value:
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

        enemy_manager.paste(my_map)
        enemy_manager.move()
        enemy_manager.ground_check(collision)
        enemy_manager.jump()

        for bubble in character.bubble:
            my_map.paste(bubble.image, bubble.position, bubble.image)
        
        character.ground_check(collision)
        character.colision_check(collision)
        result=character.enemy_hit(enemy_manager.enemy)

        if result == -2:
            pass
        elif result == -1:
            character.life -= 1
            score -= 100
            character.respawn()
        else:
            score += 300
            enemy_manager.enemy.pop(result)

        score += character.bubble_hit(enemy_manager.enemy)
        
        for life in range(character.life):
            my_map.paste(character.life_image, (60+(life*10), 5 ,70+(life*10) , 15 ), character.life_image)

        my_map.paste(character.image, character.position, character.image)

        if len(enemy_manager.enemy)==0:
            joystick.disp.image(game_clear)
            

        if character.life < 0 :
            joystick.disp.image(game_over)
            exit(0)

        joystick.disp.image(my_map)
        
if __name__ == '__main__':
    main()