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
Deck2=[0,0,0,0,0,0,0,0,0,0,0,0]
Deck3=[0,0,0,0,0,0,0,0,0,0,0,0]
Deck_y=[230,230,230,230,230,230,165,165,165,165,165,165]
mouse_x,mouse_y=0,0
skill1cheak=0
skill2cheak=0
skill3cheak=0
lastcheak=0
common1cheak=0
common2cheak=0
common3cheak=0
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
    global skill1cheak,skill2cheak,skill3cheak,lastcheak,common1cheak,common2cheak,common3cheak
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y=event.x, 600- event.y
        if event.type ==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                Deckcheak1=0
                skill1cheak, skill2cheak, skill3cheak, lastcheak, common1cheak, common2cheak, common3cheak=0,0,0,0,0,0,0
                game_framework.push_state(CharacterSelection)
            elif(event.type, event.button)==(SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
                if skill1cheak <3and Deckcheak1<12 and mouse_x > 75 and mouse_x < 125 and mouse_y > 365 and mouse_y < 435:
                    Deck3[Deckcheak1] = 0
                    Deck2[Deckcheak1] = 0
                    Deckcheak1 += 1
                    skill1cheak += 1
                if skill2cheak <3 and Deckcheak1<12 and mouse_x > 175 and mouse_x < 225 and mouse_y > 365 and mouse_y < 435:
                    Deck3[Deckcheak1] = 45
                    Deck2[Deckcheak1] = 0
                    Deckcheak1 += 1
                    skill2cheak += 1
                if skill3cheak <3 and Deckcheak1<12 and mouse_x > 275 and mouse_x < 325 and mouse_y > 365 and mouse_y < 435:
                    Deck3[Deckcheak1] = 90
                    Deck2[Deckcheak1] = 0
                    Deckcheak1 += 1
                    skill3cheak += 1
                if lastcheak<2 and Deckcheak1<12 and mouse_x > 375 and mouse_x < 425 and mouse_y > 365 and mouse_y < 435:
                    Deck3[Deckcheak1] = 135
                    Deck2[Deckcheak1] = 0
                    Deckcheak1 += 1
                    lastcheak += 1
                if common1cheak <3 and Deckcheak1<12 and mouse_x > 125 and mouse_x < 175 and mouse_y > 165 and mouse_y < 235:
                    Deck2[Deckcheak1] = 65
                    Deck3[Deckcheak1] = 0
                    Deckcheak1 += 1
                    common1cheak += 1
                if common2cheak <3 and Deckcheak1<12 and mouse_x > 225 and mouse_x < 275 and mouse_y > 165 and mouse_y < 235:
                    Deck2[Deckcheak1] = 65
                    Deck3[Deckcheak1] = 45
                    Deckcheak1 += 1
                    common2cheak += 1
                if common3cheak <3 and Deckcheak1<12 and mouse_x > 325 and mouse_x < 375 and mouse_y > 165 and mouse_y < 235:
                    Deck2[Deckcheak1] = 65
                    Deck3[Deckcheak1] = 90
                    Deckcheak1 += 1
                    common3cheak += 1
                if Deckcheak1==12 and mouse_x > 625 and mouse_x < 750 and mouse_y>450and mouse_y<550:
                    game_framework.push_state(BackgroundSelection)



def draw():
    global Deck1,Deck2,Deckcheak1,Deckcheak2
    Deck1 = 0
    clear_canvas()
    if character ==0:
        reimu.draw(400,300)
        for D in range(0, 4):
            reimuDeck.clip_draw(45*D,0,45,65,100*(D+1),400)
        for C in range(0,3):
            commonDeck.clip_draw(45*C, 0, 45, 65, 50+100*(C+1), 200)

    elif character ==1:
        marisa.draw(400,300)
        for D in range(0, 4):
            marisaDeck.clip_draw(45*D,0,45,65,100*(D+1),400)
        for C in range(0,3):
            commonDeck.clip_draw(45*C, 0, 45, 65, 50+100*(C+1), 200)

    elif character ==2:
        iku.draw(400,300)
        for D in range(0, 4):
            ikuDeck.clip_draw(45*D,0,45,65,100*(D+1),400)
        for C in range(0,3):
            commonDeck.clip_draw(45*C, 0, 45, 65, 50+100*(C+1), 200)

    elif character ==3:
        tenshi.draw(400,300)
        for D in range(0, 4):
            tenshiDeck.clip_draw(45*D,0,45,65,100*(D+1),400)
        for C in range(0,3):
            commonDeck.clip_draw(45*C, 0, 45, 65, 50+100*(C+1), 200)


    next.draw(700,500)
    for Deck1 in range(0,Deckcheak1):
        if character == 0:
            reimuDeck.clip_draw(Deck3[Deck1], Deck2[Deck1], 45, 65, 510 + 45 * (Deck1 % 6), Deck_y[Deck1])
        elif character == 1:
            marisaDeck.clip_draw(Deck3[Deck1], Deck2[Deck1], 45, 65, 510 + 45 * (Deck1 % 6), Deck_y[Deck1])
        elif character == 2:
            ikuDeck.clip_draw(Deck3[Deck1], Deck2[Deck1], 45, 65, 510+45*(Deck1%6), Deck_y[Deck1])
        elif character == 3:
            tenshiDeck.clip_draw(Deck3[Deck1], Deck2[Deck1], 45, 65, 510+45*(Deck1%6), Deck_y[Deck1])




    
    update_canvas()






def update():
    global character,Enemycharacter
    Enemycharacter = random.randint(0, 3)


def pause():
    global character


def resume():
    pass
