from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb

from Character import Character
from Joystick import Joystick
from BubbleManager import BubbleManager
from Bubble import Bubble

def main():
    joystick = Joystick()
    character = Character()
    map = Image.open("./res/map2.png").resize((240,240))
    pressed=False
    a=0
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
        for bubble in character.bubble:
            my_map.paste(bubble.image, bubble.position, bubble.image)
        character.mov_bubble()
        my_map.paste(character.image, character.position, character.image)
        joystick.disp.image(my_map)
        
if __name__ == '__main__':
    main()