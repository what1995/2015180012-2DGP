import random
import json
import os

from pico2d import *
import game_framework
import game_world
import CharacterSelection
from iku import Iku
from reimu import Reimu
from tenshi import Tenshi
from marisa import Marisa
from background import BackGround
from PlayerHP import Player_HP
from EnemyHP import Enemy_HP


name = "MainState"

iku = None
reimu=None
tenshi=None
marisa=None
grass = None
Player = 0
def enter():
    global iku, background, Player,reimu,tenshi,marisa,PlayerHP,EnemyHP
    if Player==0:
        iku = Iku()
        game_world.add_object(iku, 1)
    elif Player==1:
        reimu = Reimu()
        game_world.add_object(reimu, 1)
    elif Player==2:
        tenshi = Tenshi()
    elif Player == 3:
        marisa = Marisa()
        game_world.add_object(marisa, 1)
    background = BackGround()
    PlayerHP=Player_HP()
    EnemyHP=Enemy_HP()
    game_world.add_object(background,0)
    game_world.add_object(PlayerHP, 0)
    game_world.add_object(EnemyHP, 0)



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
            if Player == 2:
                tenshi.handle_event(event)
            if Player == 3:
                marisa.handle_event(event)


def update():
    for game_objcet in game_world.all_objects():
        game_objcet.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







