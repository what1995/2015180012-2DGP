import game_framework
import random
from pico2d import *
import main_state
import os

os.chdir('C:\\2DGP\\2015180012-2DGP\\Project\\FCGimage')
#import CharacterSelection
import game_world

name = "characterSelection"
image = None
start = None
character = None
Enemycharacter=None
def enter():
    global image,character
    global start
    image = load_image('CharacterSelection.png')

def exit():
    global image
    global start
    del(image)
    del(start)


def handle_events():
    global character,Enemycharacter
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                character=3

                game_framework.push_state(main_state)


def draw():
    clear_canvas()
    image.draw(400,300)
    
    update_canvas()






def update():
    global character,Enemycharacter
    Enemycharacter = random.randint(0, 3)
    character = 1


def pause():
    global character


def resume():
    pass
