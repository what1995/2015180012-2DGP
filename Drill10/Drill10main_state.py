import random
import json
import os

from pico2d import *

import game_framework
import Drill10title_state



name = "Drill10MainState"

boy = None
grass = None
font = None

PAUSE =False

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.cheak=1
        self.image = load_image('animation_sheet.png')
        self.dir = 1

    def update(self):
         self.frame = (self.frame + 1) % 8
         self.x += self.dir*5
         if self.x >= 800:
            self.dir = -1
            self.cheak=0
         elif self.x <= 0:
            self.dir = 1
            self.cheak=1
         delay(0.03)

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.cheak*100, 100, 100, self.x, self.y)


def enter():
    global boy,grass
    boy =Boy()
    grass = Grass()



def exit():
    global boy,grass
    del(boy)
    del(grass)


def pause():
    pass

def resume():
    pass


def handle_events():
    global  PAUSE
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif  event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(Drill10title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            pause()


def update():
    boy.update()



def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()




