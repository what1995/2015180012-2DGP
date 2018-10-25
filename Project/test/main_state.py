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
from Enemy_marisa import Enemy_Marisa
from Enemy_reimu import Enemy_Reimu
from Enemy_tenshi import Enemy_Tenshi
from Enemy_iku import Enemy_Iku
name = "MainState"

iku = None
reimu=None
tenshi=None
marisa=None
grass = None
Enemy_marisa=None
Enemy_reimu =None
Enemy_tenshi=None
Enemy_iku=None
Player = 2
def enter():
    global iku, background, Player,reimu,tenshi,marisa,PlayerHP,EnemyHP,Enemy_marisa,Enemy_reimu,Enemy_tenshi,Enemy_iku
    if Player==0:
        iku = Iku()

        Enemy_marisa=Enemy_Marisa()

        game_world.add_object(Enemy_marisa, 1)

        game_world.add_object(iku, 1)

    elif Player==1:
        reimu = Reimu()

        game_world.add_object(reimu, 1)

        Enemy_reimu = Enemy_Reimu()

        game_world.add_object(Enemy_reimu, 1)
    elif Player==2:
        tenshi = Tenshi()

        game_world.add_object(tenshi, 1)

        Enemy_iku=Enemy_Iku()

        game_world.add_object(Enemy_iku, 1)

    elif Player == 3:
        marisa = Marisa()

        game_world.add_object(marisa, 1)

        Enemy_tenshi=Enemy_Tenshi()

        game_world.add_object(Enemy_tenshi, 1)
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

                Enemy_marisa.handle_event(event)

            if Player == 1:
                reimu.handle_event(event)

                Enemy_reimu.handle_event(event)

            if Player == 2:
                tenshi.handle_event(event)

                Enemy_iku.handle_event(event)
            if Player == 3:
                marisa.handle_event(event)

                Enemy_tenshi.handle_event(event)


def update():
    for game_objcet in game_world.all_objects():
        game_objcet.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







