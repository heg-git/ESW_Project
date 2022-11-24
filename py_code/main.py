from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb

from Character import Character
from Joystick import Joystick

def main():
    
    joystick = Joystick()
    character = Character()

    map = Image.open("./res/map2.png").resize((240,240))    
    while True:
        my_map=map.copy()
    # if not joystick.button_U.value:  # up pressed
    #     character.move('up')

    # if not joystick.button_D.value:  # down pressed
    #     character.move('down')

        if not joystick.button_L.value:  # left pressed
            character.move('left')

        if not joystick.button_R.value:  # right pressed
            character.move('right')

        if not joystick.button_B.value:
            character.state = 'jump'

        if character.state == 'jump':
            character.jump()
        
        if not joystick.button_A.value:  # right pressed
            character.attack()
        
        my_map.paste(character.image, character.position, character.image)
        joystick.disp.image(my_map)
        
if __name__ == '__main__':
    main()