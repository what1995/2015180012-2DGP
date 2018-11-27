import random
import json
import pickle
import os
from pico2d import *
import game_framework
import game_world
import End
import world_build_state

name = "MainState"

boy_die =True


score=0
def enter():
    # game world is prepared already in world_build_state
    global boy,boy_die,score
    boy_die=True
    boy = world_build_state.get_boy()

    pass

def exit():
    game_world.clear()

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
            game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            game_world.save()
        else:
            boy.handle_event(event)
        if boy_die==False:
            game_world.rank_list.append(score)
            game_world.rank_list.sort()
            game_framework.change_state(End)


def update():
    global score
    for game_object in game_world.all_objects():
        game_object.update()
    score = str((get_time() - boy.start_time))




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






