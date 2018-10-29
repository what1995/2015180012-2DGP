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
Deckcheak1=0
Deck1=0
Deckcheak2=0
Deck2=0
mouse_x,mouse_y=0,0
def enter():
    global iku,reimu,tenshi,marisa,character,Enemycharacter
    global reimuDeck,marisaDeck,ikuDeck,tenshiDeck,commonDeck
    global next
    reimu= load_image('Reimu-Deck.png')
    reimuDeck= load_image('RimuSpellCard.png')
    marisa= load_image('Marisa-Deck.png')
    marisaDeck= load_image('MarisaSpellCard.png')
    iku = load_image('Iku-Deck.png')
    ikuDeck= load_image('IkuSpellCard.png')
    tenshi = load_image('Tensi-Deck.png')
    tenshiDeck= load_image('TenshiSpellCard.png')
    next=load_image('Deck_Next.png')
    commonDeck=load_image('commonCard.png')
    character = CharacterSelection.character


def exit():
    global iku, reimu, tenshi, marisa



def handle_events():
    global character,Enemycharacter,Deckcheak,mouse_x,mouse_y,Deckcheak1,Deckcheak2
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y=event.x, 600- event.y
        if event.type ==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                Deckcheak1=0
                game_framework.push_state(CharacterSelection)
            elif(event.type, event.button)==(SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
                if Deckcheak1 <7:
                    Deckcheak1 += 1
                if Deckcheak1==7 and Deckcheak2 <6:
                    Deckcheak2 += 1
                if mouse_x > 625 and mouse_x < 750 and mouse_y>450and mouse_y<550:
                    game_framework.push_state(BackgroundSelection)



def draw():
    global Deck1,Deck2,Deckcheak1,Deckcheak2
    Deck1 = 0
    Deck2=0
    clear_canvas()
    if character ==0:
        reimu.draw(400,300)
        reimuDeck.clip_draw(0,0,45,65,100,400)
        reimuDeck.clip_draw(45, 0, 45, 65, 200, 400)
        reimuDeck.clip_draw(90, 0, 45, 65, 300, 400)
        reimuDeck.clip_draw(135, 0, 45, 65, 400, 400)
        commonDeck.clip_draw(0, 0, 45, 65, 150, 200)
        commonDeck.clip_draw(45, 0, 45, 65, 250, 200)
        commonDeck.clip_draw(90, 0, 45, 65, 350, 200)
    elif character ==1:
        marisa.draw(400,300)
        marisaDeck.clip_draw(0, 0, 45, 65, 100, 400)
        marisaDeck.clip_draw(45, 0, 45, 65, 200, 400)
        marisaDeck.clip_draw(90, 0, 45, 65, 300, 400)
        marisaDeck.clip_draw(135, 0, 45, 65, 400, 400)
        commonDeck.clip_draw(0, 0, 45, 65, 150, 200)
        commonDeck.clip_draw(45, 0, 45, 65, 250, 200)
        commonDeck.clip_draw(90, 0, 45, 65, 350, 200)
    elif character ==2:
        iku.draw(400,300)
        ikuDeck.clip_draw(0, 0, 45, 65, 100, 400)
        ikuDeck.clip_draw(45, 0, 45, 65, 200, 400)
        ikuDeck.clip_draw(90, 0, 45, 65, 300, 400)
        ikuDeck.clip_draw(135, 0, 45, 65, 400, 400)
        commonDeck.clip_draw(0, 0, 45, 65, 150, 200)
        commonDeck.clip_draw(45, 0, 45, 65, 250, 200)
        commonDeck.clip_draw(90, 0, 45, 65, 350, 200)
    elif character ==3:
        tenshi.draw(400,300)
        tenshiDeck.clip_draw(0, 0, 45, 65, 100, 400)
        tenshiDeck.clip_draw(45, 0, 45, 65, 200, 400)
        tenshiDeck.clip_draw(90, 0, 45, 65, 300, 400)
        tenshiDeck.clip_draw(135, 0, 45, 65, 400, 400)
        commonDeck.clip_draw(0, 0, 45, 65, 150, 200)
        commonDeck.clip_draw(45, 0, 45, 65, 250, 200)
        commonDeck.clip_draw(90, 0, 45, 65, 350, 200)

    next.draw(700,500)
    for Deck1 in range(0,Deckcheak1):
        ikuDeck.clip_draw(0, 0, 45, 65, 510+45*(Deck1%6), 230)
    for Deck2 in range(0,Deckcheak2):
        ikuDeck.clip_draw(45, 0, 45, 65, 510 + 45 * (Deck2 % 6), 165)


    
    update_canvas()






def update():
    global character,Enemycharacter
    Enemycharacter = random.randint(0, 3)


def pause():
    global character


def resume():
    pass
