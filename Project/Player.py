from pico2d import *
import os

os.chdir('C:\\2DGP\\2015180012-2DGP\\Project\\FCGimage')
class BackGround:
    def __init__(self):
        self.x, self.y = 400, 300
        self.backgroundselection = 1
        self.Shrine = load_image('Hakurei Shrine.png')
        self.Bamboo = load_image('bamboo.png')
        self.Clock = load_image('clock tower.png')

    def draw(self):
        if self.backgroundselection ==1:
            self.Shrine.draw(self.x,self.y)
        if self.backgroundselection == 2:
            self.Bamboo.draw(self.x, self.y)
        if self.backgroundselection == 3:
            self.Clock.draw(self.x, self.y)


class Player:
    def __init__(self):
        self.Player = 200
        self.Enemy =600
        self.All_Y=200
        self.stat =40  ##10 레이무 20 이쿠 30 텐시 40 마리사
######################STANDING##################################
        self.MStanding = load_image('MarisaStanding-Motion.png')
        self.Standi = 0
        self.Standj = 0
        self.Standcheak =0


######################SKILL1####################################




######################SKILL2####################################






######################SKILL3####################################




######################LASTSPELL####################################

        self.MLastspell = load_image('MarisaLastspell-Motion.png')
        self.Lastspelli = 0
        self.Lastspellj = 0
        self.Lastspellcheak = 0
        self.MLastspellEffect = load_image('MarisaLastspell.png')
        self.LastspellEframe1 = 0

    def update(self):
        if self.stat==40:
            if self.Standcheak < 10:
                self.Standi = (self.Standi+1) % 11
                self.Standj = (self.Standj+1) % 10
                self.Standcheak += 1
            if self.Standcheak == 9:
                self.Standi = 0
                self.Standj= 0
                self.Standcheak = 0
        if self.stat==44:
            if self.Lastspellcheak < 18:
                self.Lastspelli = (self.Lastspelli + 1) % 17
                self.Lastspellj = (self.Lastspellj + 1) % 17
                if self.Lastspellcheak > 4:
                    if self.Lastspellcheak < 11:
                        # Player
                        self.MLastspellEffect.clip_draw(self.LastspellEframe1 * 261, 250, 260, 250, self.Player + 400,
                                                       self.All_Y - 10)
                        # Enemy
                     #   self.LastspellEffect.clip_draw(self.LastspellEframe1 * 261, 0, 260, 250, self.Enemy - 400,self.All_Y)
                        self.MLastspellEframe1 = (self.LastspellEframe1 + 1) % 7
                self.Lastspellcheak += 1

            if self.Lastspellcheak == 18:
                self.Lastspelli = 0
                self.Lastspellj = 0
                self.Lastspellcheak = 0
                player.stat = 40



    def Stand(self):
        if self.stat==40:
            self.Standframe1 = [0,65,126,188,250,312,372,434,495,556,618]
            self.Standframe2 = [65,61,62,62,62,60,62,61,60,62]
          #플레이어
            self.MStanding.clip_draw(self.Standframe1[self.Standi], 110, self.Standframe2[self.Standj], 110, self.Player,self.All_Y )
          #적
         #   self.Standing.clip_draw(self.Standframe1[self.Standi], 0, self.Standframe2[self.Standj], 110, self.Enemy,self.All_Y)

        if self.stat == 44:
            self.Lastframe1 = [0, 65,127,187,251,305,386,451,536,610,680,750,815,880,943,1010,1070]
            self.Lastframe2 = [65,62,60,64,55,79,62,80,72,66,66,65,63,60,59,58,58]

        # 플레이어
            self.MLastspell.clip_draw(self.Lastframe1[self.Lastspelli], 120, self.Lastframe2[self.Lastspellj], 120, self.Player+250,self.All_Y)
        # 적
         #   self.Lastspell.clip_draw(self.Lastframe1[self.Lastspelli], 0, self.Lastframe2[self.Lastspellj], 120, self.Enemy-250,self.All_Y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            player.stat = 44
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            background.backgroundselection = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            background.backgroundselection = 2
        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            background.backgroundselection = 3


open_canvas()
background=BackGround()
player=Player()

running=True

while running:

    handle_events()
    clear_canvas()
    background.draw()
    player.update()

    player.Stand()
    
    update_canvas()
    delay(0.1)
# finalization code
close_canvas()
