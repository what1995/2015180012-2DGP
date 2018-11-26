import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import world_build_state as start_state
import main_state


#from ranking import Ranking


boy = None


name = "End"




def enter():
    pass
    pass



def exit():
    pass

def pause():
    pass

def resume():
    pass

def create_new_world():
    pass


def load_saved_world():
    pass
    # fill here


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(start_state)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






