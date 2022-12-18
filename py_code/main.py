from PIL import Image, ImageDraw, ImageFont
from Character import Character
from EnemyManager import EnemyManager
from Boss import Boss
from MapCollision import MapCollision
from Joystick import Joystick

#main
def main():
    
    #game setting section
    fnt1 = ImageFont.truetype("./res/etc/DungGeunMo.ttf", 20)
    fnt2 = ImageFont.truetype("./res/etc/DungGeunMo.ttf", 16)
    fnt3 = ImageFont.truetype("./res/etc/DungGeunMo.ttf", 15)
    fnt4 = ImageFont.truetype("./res/etc/DungGeunMo.ttf", 40)
    fnt5 = ImageFont.truetype("./res/etc/DungGeunMo.ttf", 25)

    #create object for game
    joystick = Joystick()
    character = Character()
    start = Image.open("./res/etc/start.png").resize((240,240))
    game_clear = Image.open("./res/etc/game_clear.png").resize((240,177))

    #stage 1 setting
    enemy_manager = EnemyManager(4, 2)
    collision = MapCollision(1)
    map = Image.open("./res/etc/map1.png").resize((240,240))

    ImageDraw.Draw(start).text((60, 180), "ESW PROJECT", font=fnt1, fill=(255,0 ,0))
    ImageDraw.Draw(start).text((27, 205),("PRESS A TO START!!") ,font=fnt1, fill=(255,255,255))
    ImageDraw.Draw(map).text((25, 2), "LIFE", font=fnt2, fill=(0,255,0))
    ImageDraw.Draw(map).text((105, 2),("HIGH SCORE "),font=fnt3, fill=(255,0,0))

    pressed = False
    score = 0
    
    #Press A button to Start
    joystick.disp.image(start)
    while True:  
        if not joystick.button_A.value:
            pressed=True
        elif joystick.button_A.value and pressed:
            pressed=False
            break

    #stage 1
    while True:

        #copy map image
        my_map=map.copy()

        #joystic button press event
        if not joystick.button_L.value:
            character.move("left")

        if not joystick.button_R.value:  
            character.move("right")

        if not joystick.button_B.value:
            character.state = "jump"

        if not joystick.button_A.value:
            pressed=True
        elif joystick.button_A.value and pressed:
            character.attack()
            score += 10
            pressed=False

        if character.state == "jump" or character.state == "fall":
            character.jump()

        #character event
        character.mov_bubble()
        character.ground_check(collision)
        character.colision_check(collision)

        #character <-> enemy event
        result=character.enemy_hit(enemy_manager.enemy)
        if result == -2:
            pass
        #monster collision
        elif result == -1:
            character.life -= 1
            score -= 100
            character.respawn()
        #kill monster
        elif result < enemy_manager.en1:
            enemy_manager.en1 -= 1
            score += 300
            enemy_manager.enemy.pop(result)
        else:
            score += 500
            enemy_manager.en2 -= 1
            enemy_manager.enemy.pop(result)
        score += character.bubble_hit(enemy_manager.enemy)

        #enemy event        
        enemy_manager.move(character.position)
        enemy_manager.ground_check(collision)
        enemy_manager.jump()


        #draw section

        #draw enemy
        enemy_manager.paste(my_map)
        #draw character
        my_map.paste(character.image, character.position, character.image)
        #draw bubble
        for bubble in character.bubble:
            my_map.paste(bubble.image, bubble.position, bubble.image)

        #draw life 
        for life in range(character.life):
            my_map.paste(character.life_image, (60+(life*10), 5, 70+(life*10) , 15), character.life_image)

        #draw score
        ImageDraw.Draw(my_map).text((190, 2), str(score),font=fnt3)
        
        #game event
        #if enemy does not exist go to next stage
        if len(enemy_manager.enemy) == 0:
            break

        #if character death 3 time game over
        elif character.life == 0 :
            ImageDraw.Draw(my_map).rectangle((0, 0, 240, 240), fill=(0, 0, 0))
            ImageDraw.Draw(my_map).text((30, 75), "GAME OVER", font=fnt4, fill=(255, 255, 255))
            ImageDraw.Draw(my_map).text((55, 145), "TRY AGAIN!", font=fnt5, fill=(255, 255, 255))
            joystick.disp.image(my_map)
            exit(0)

        #display on screen
        joystick.disp.image(my_map)


    #stage 2 setting
    map = Image.open("./res/etc/map2.png").resize((240,240))
    character.respawn()
    
    #create object for stage2
    boss = []
    boss.append(Boss())
    enemy_manager=EnemyManager(2,1)
    collision = MapCollision(2)

    ImageDraw.Draw(map).text((25, 2), "LIFE", font=fnt2, fill=(0,255,0))
    ImageDraw.Draw(map).text((105, 2),("HIGH SCORE "),font=fnt3, fill=(255,0,0))    

    #stage 2
    while True:        
        #copy map
        my_map=map.copy()
        #joystic button press event
        if not joystick.button_L.value:
            character.move("left")

        if not joystick.button_R.value:  
            character.move("right")

        if not joystick.button_B.value:
            character.state = "jump"

        if not joystick.button_A.value:
            pressed=True
        elif joystick.button_A.value and pressed:
            character.attack()
            score += 10
            pressed=False

        if character.state == "jump" or character.state == "fall":
                character.jump()
        
        #character event
        character.mov_bubble()
        character.ground_check(collision)
        character.colision_check(collision)
        
        #character <-> boss event
        result = character.enemy_hit(boss)
        #boss collision
        if result == -1:
            character.life -= 1
            score -= 100
            character.respawn()
        #kill boss
        elif result == 0:
            score += 5000
            boss.pop(result)
        score+=character.bubble_hit(boss)
        
        #if boss killed disp clear stage and exit
        if len(boss)==0:
            ImageDraw.Draw(my_map).rectangle((0, 0, 240, 240), fill=(0, 0, 0))
            my_map.paste(game_clear)
            ImageDraw.Draw(my_map).text((20, 45), "GAME CLEAR", font=fnt4, fill=(255, 255, 255))
            ImageDraw.Draw(my_map).text((42, 185), "CONGRATULATIONS!", font=fnt1, fill=(255, 255, 255))
            joystick.disp.image(my_map)
            exit(0)
        
        #character <-> enemy event
        result = character.enemy_hit(enemy_manager.enemy)
        if result == -2:
            pass
        #enemy collision
        elif result == -1:
            character.life -= 1
            score -= 100
            character.respawn()
        #kill enemy
        elif result < enemy_manager.en1:
            enemy_manager.en1 -= 1
            score += 300
            enemy_manager.enemy.pop(result)
        else:
            score += 500
            enemy_manager.en2 -= 1
            enemy_manager.enemy.pop(result)
        score += character.bubble_hit(enemy_manager.enemy)

        #enemy event
        enemy_manager.move(character.position)
        enemy_manager.ground_check(collision)
        enemy_manager.jump()
        boss[0].move()
    
        #draw section
        
        #draw boss
        my_map.paste(boss[0].image, boss[0].position, boss[0].image)
        
        #draw enemy
        enemy_manager.paste(my_map)

        #draw character
        my_map.paste(character.image, character.position, character.image)
        
        #draw bubble
        for bubble in character.bubble:
            my_map.paste(bubble.image, bubble.position, bubble.image)

        #draw life
        for life in range(character.life):
            my_map.paste(character.life_image, (60+(life*10), 5 ,70+(life*10) , 15 ), character.life_image)
        
        #draw score
        ImageDraw.Draw(my_map).text((190, 2), str(score),font=fnt3)

        #draw boss status
        ImageDraw.Draw(my_map).text((102, 30), "DRUNK", font=fnt3, fill=(255, 255, 255))
        if boss[0].hp>0:
            ImageDraw.Draw(my_map).rectangle((30, 47, 6*boss[0].hp+30, 51), fill=(255, 0, 0))

        #disp game over
        if character.life < 0 :
            ImageDraw.Draw(my_map).rectangle((0, 0, 240, 240), fill=(0, 0, 0))
            ImageDraw.Draw(my_map).text((30, 75), "GAME OVER", font=fnt4, fill=(255, 255, 255))
            ImageDraw.Draw(my_map).text((55, 145), "TRY AGAIN!", font=fnt5, fill=(255, 255, 255))
            joystick.disp.image(my_map)
            exit(0)

        joystick.disp.image(my_map)
        
if __name__ == '__main__':
    main()