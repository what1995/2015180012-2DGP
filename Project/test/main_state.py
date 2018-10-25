import random
import json
import os

from pico2d import *
import game_framework
import game_world

from iku import Iku
from reimu import Reimu
from background import BackGround



name = "MainState"

iku = None
reimu=None
grass = None
Player = 1
def enter():
    global iku, background, Player,reimu
    if Player==0:
        iku = Iku()
        game_world.add_object(iku, 1)
    elif Player==1:
        reimu = Reimu()
        game_world.add_object(reimu, 1)
    background = BackGround()
    game_world.add_object(background,0)



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
                game_framework.quit()
        else:
            if Player == 0:
                iku.handle_event(event)
            if Player == 1:
                reimu.handle_event(event)


def update():
    for game_objcet in game_world.all_objects():
        game_objcet.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







