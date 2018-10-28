import game_framework
import random
from pico2d import *
import CharacterSelection
import BackgroundSelection
import main_state
import os

os.chdir('C:\\2DGP\\2015180012-2DGP\\Project\\FCGimage')
#import CharacterSelection
import game_world

name = "deckSelection"
image = None
next = None
character = None
Enemycharacter=None
Enemycharacter=None
def enter():
    global iku,reimu,tenshi,marisa,character,Enemycharacter
    global next
    reimu= load_image('Reimu-Deck.png')
    marisa= load_image('Marisa-Deck.png')
    iku = load_image('Iku-Deck.png')
    tenshi = load_image('Tensi-Deck.png')
    next=load_image('Deck_Next.png')
    character = CharacterSelection.character


def exit():
    global iku, reimu, tenshi, marisa



def handle_events():
    global character,Enemycharacter
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.push_state(CharacterSelection)
            elif(event.type, event.button)==(SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
                if event.x > 625 and event.x < 750 and 600- event.y>450and 600- event.y<550:
                    game_framework.push_state(BackgroundSelection)



def draw():

    clear_canvas()
    if character ==0:
        reimu.draw(400,300)
    elif character ==1:
        marisa.draw(400,300)
    elif character ==2:
        iku.draw(400,300)
    elif character ==3:
        tenshi.draw(400,300)

    next.draw(700,500)

    
    update_canvas()






def update():
    global character,Enemycharacter
    Enemycharacter = random.randint(0, 3)


def pause():
    global character


def resume():
    pass
