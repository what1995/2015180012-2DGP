import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import world_build_state as start_state

boy = None


name = "End"

menu = None
font=None

def enter():
    global menu,font
    menu = load_image('BGbamboo.png')
    font = load_font('ENCR10B.TTF', 20)
    pass
def exit():
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(start_state)


def update():
    pass

def draw():
    global font,i
    i = 200
    j=750
    clear_canvas()
    for a in game_world.rank_list:
        b=float(a)
        i+=50
        font.draw(150,i,'(%3.2f)'%b, (255, 0, 0))
    for a in range(1,11):
        j-=50
        font.draw(20,j,'(%1d)'%a, (255, 0, 0))

    update_canvas()






