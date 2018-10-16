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
        self.stat =10  ##10 레이무 20 이쿠 30 텐시 40 마리사
######################STANDING##################################
        self.MStanding = load_image('MarisaStanding-Motion.png')
        self.RStanding = load_image('Reimu-Standing-Motion.png')
        self.Standi = 0
        self.Standj = 0
        self.Standcheak =0
        self.frame=0


######################SKILL1####################################
        self.MSkill1 = load_image('MarisaSkill1-Motion.png')
        self.RSKill1 = load_image('Reimu-Skill1-Motion.png')
        self.Skill1i = 0
        self.Skill1j = 0
        self.Skill1cheak = 0
        self.MS1Effect = load_image('MarisaSkill1.png')
        self.RS1Effect = load_image('Reimu-Skill1.png')
        self.Skill1Ei = 0
        self.Skill1Ej = 0
        self.Skill1X=80
        self.S1frame=0
        self.Skill1Eframe1 = 0




######################SKILL2####################################
        self.MSkill2 = load_image('MarisaSkill2-Motion.png')
        self.Skill2i = 0
        self.Skill2j = 0
        self.Skill2cheak = 0
        self.MS2Effect = load_image('MarisaSkill2.png')
        self.Skill2Ex1 = 120
        self.Skill2Ex2 = 100
        self.Skill2Ex3 = 80






######################SKILL3####################################
        self.MSkill3 = load_image('MarisaSkill3-Motion.png')
        self.Skill3i = 0
        self.Skill3j = 0
        self.Skill3cheak = 0
        self.MS3Effect = load_image('MarisaSKill3.png')
        self.Skill3Eframe1 = 0
        self.Skill3Ex1 = 120




######################LASTSPELL####################################

        self.MLastspell = load_image('MarisaLastspell-Motion.png')
        self.Lastspelli = 0
        self.Lastspellj = 0
        self.Lastspellcheak = 0
        self.MLastspellEffect = load_image('MarisaLastspell.png')
        self.LastspellEframe1 = 0

    def update(self):

        #####STANDING#########
        if self.stat==10:
            if self.Standcheak<12:
                self.frame =(self.frame+1)%11
                self.Standcheak += 1
            if self.Standcheak == 11:
                self.frame = 0
                self.Standcheak = 0
        if self.stat==40:
            if self.Standcheak < 10:
                self.Standi = (self.Standi+1) % 11
                self.Standj = (self.Standj+1) % 10
                self.Standcheak += 1
            if self.Standcheak == 9:
                self.Standi = 0
                self.Standj= 0
                self.Standcheak = 0

        #####SKILL1#########

             ##레이무
        if self.stat ==11:
            if self.Skill1cheak<12:
                self.RS1Effect.clip_draw(self.S1frame * 70, 0, 80, 110, self.Player + self.Skill1X, self.All_Y)
                self.Skill1i = (self.Skill1i + 1) % 13
                self.Skill1j = (self.Skill1j + 1) % 12
                self.S1frame = (self.S1frame + 1) % 13
                self.Skill1X = self.Skill1X+ 30
            self.Skill1cheak += 1
            if self.Skill1cheak == 12:
                self.Skill1i = 0
                self.Skill1j = 0
                self.Skill1cheak = 0
                self.Skill1X=80
                self.S1frame=0
                self.Skill1Eframe1 = 0
                player.stat = 10



            ###마리사
        if self.stat ==41:
            if self.Skill1cheak < 18:
                if self.Skill1cheak < 6:
                    self.Skill1i = (self.Skill1i + 1) % 10
                    self.Skill1j = (self.Skill1j + 1) % 9
                if self.Skill1cheak > 6:
                    # Player
                    self.MS1Effect.clip_draw(self.Skill1Eframe1 * 260, 0, 260, 505, self.Enemy, self.All_Y + 150)
                    if self.Skill1cheak < 15:
                        self.Skill1Eframe1 = (self.Skill1Eframe1 + 1) % 9
                    if self.Skill1cheak >= 15:
                        self.Skill1i = (self.Skill1i + 1) % 10
                        self.Skill1j = (self.Skill1j + 1) % 9
                self.Skill1cheak += 1
            if self.Skill1cheak == 18:
                self.Skill1i = 0
                self.Skill1j = 0
                self.Skill1cheak = 0
                self.Skill1Eframe1 = 0
                player.stat = 40

        #####SKILL2#########
        if self.stat ==42:
            if self.Skill2cheak < 7:
                self.Skill2i = (self.Skill2i + 1) % 8
                self.Skill2j = (self.Skill2j + 1) % 7
                # Player
                self.MS2Effect.clip_draw(0, 125, 132, 125, self.Player + self.Skill2Ex1, self.All_Y)
                self.MS2Effect.clip_draw(132, 125, 132, 125, self.Player + self.Skill2Ex2, self.All_Y)
                self.MS2Effect.clip_draw(264, 125, 132, 125, self.Player + self.Skill2Ex3, self.All_Y)
                self.Skill2Ex1 += 75
                self.Skill2Ex2 += 75
                self.Skill2Ex3 += 75
                self.Skill2cheak += 1

            if self.Skill2cheak == 7:
                self.Skill2i = 0
                self.Skill2j = 0
                self.Skill2Ex1 = 120
                self.Skill2Ex2 = 100
                self.Skill2Ex3 = 80
                self.Skill2cheak = 0
                player.stat=40

        #####SKILL3#########
        if self.stat==43:
            if self.Skill3cheak < 17:
                if self.Skill3cheak < 7:
                    self.Skill3i = (self.Skill3i + 1) % 10
                    self.Skill3j = (self.Skill3j + 1) % 10
                if self.Skill3cheak >= 7:
                    self.MS3Effect.clip_draw(self.Skill3Eframe1 * 260, 255, 260, 255, self.Player + self.Skill3Ex1,self.All_Y)
                    self.Skill3Eframe1 = (self.Skill3Eframe1 + 1) % 3
                    self.Skill3Ex1 += 80
                if self.Skill3cheak >= 13:
                    self.Skill3i = (self.Skill3i + 1) % 10
                    self.Skill3j = (self.Skill3j + 1) % 10
                self.Skill3cheak += 1

            if self.Skill3cheak == 17:
                self.Skill3i = 0
                self.Skill3j = 0
                self.Skill3Ex1 = 120
                self.Skill3cheak = 0
                player.stat=40

        #####LASTSPELL#########
        if self.stat==44:
            if self.Lastspellcheak < 18:
                self.Lastspelli = (self.Lastspelli + 1) % 17
                self.Lastspellj = (self.Lastspellj + 1) % 17
                if self.Lastspellcheak > 4:
                    if self.Lastspellcheak < 11:
                        # Player
                        self.MLastspellEffect.clip_draw(self.LastspellEframe1 * 261, 250, 260, 250, self.Player + 400,self.All_Y - 10)
                        # Enemy
                     #   self.LastspellEffect.clip_draw(self.LastspellEframe1 * 261, 0, 260, 250, self.Enemy - 400,self.All_Y)
                        self.MLastspellEframe1 = (self.LastspellEframe1 + 1) % 7
                self.Lastspellcheak += 1

            if self.Lastspellcheak == 18:
                self.Lastspelli = 0
                self.Lastspellj = 0
                self.Lastspellcheak = 0
                self.LastspellEframe1=0
                player.stat = 40



    def Stand(self):

        ####STANDING########
        if self.stat==10:
            self.RStanding.clip_draw(self.frame *100,105,97,105,self.Player,self.All_Y)
        if self.stat==40:
            self.Standframe1 = [0,65,126,188,250,312,372,434,495,556,618]
            self.Standframe2 = [65,61,62,62,62,60,62,61,60,62]
          #플레이어
            self.MStanding.clip_draw(self.Standframe1[self.Standi], 110, self.Standframe2[self.Standj], 110, self.Player,self.All_Y )
        #####SKILL1#########
        ###레이무
        if self.stat==11:
            self.Skill1frame1 = [0,108,213,327,434,541,638,787,936,1080,1215,1319,1425]
            self.Skill1frame2 = [108,105,114,107,107,97,149,149,144,135,104,106]

            self.RSKill1.clip_draw(self.Skill1frame1[self.Skill1i], 110, self.Skill1frame2[self.Skill1j], 110, self.Player, self.All_Y)

        ###마리사
        if self.stat==41:
            self.Skill1frame1 = [0, 71, 132, 197, 262, 322, 396, 468, 536, 600]
            self.Skill1frame2 = [71, 61, 65, 65, 58, 72, 72, 66, 60]
            # 플레이어
            self.MSkill1.clip_draw(self.Skill1frame1[self.Skill1i], 105, self.Skill1frame2[self.Skill1j], 105,self.Player, self.All_Y)
        #####SKILL2#########
        if self.stat==42:
            self.Skill2frame1 = [0, 85, 165, 240, 318, 395, 464, 525]
            self.Skill2frame2 = [85, 80, 75, 78, 76, 67, 64]

            # 플레이어
            self.MSkill2.clip_draw(self.Skill2frame1[self.Skill2i], 120, self.Skill2frame2[self.Skill2j], 120,self.Player, self.All_Y)

        #####SKILL3#########
        if self.stat ==43:
            self.Skill3frame1 = [0, 65, 125, 195, 275, 332, 412, 500, 590, 661]
            self.Skill3frame2 = [65, 60, 70, 80, 60, 76, 85, 89, 68, 61]

            # 플레이어
            self.MSkill3.clip_draw(self.Skill3frame1[self.Skill3i], 110, self.Skill3frame2[self.Skill3j], 110,self.Player, self.All_Y)

        #####LASTSPELL#########
        if self.stat == 44:
            self.Lastframe1 = [0, 65,127,187,251,305,386,451,536,610,680,750,815,880,943,1010,1070]
            self.Lastframe2 = [65,62,60,64,55,79,62,80,72,66,66,65,63,60,59,58,58]

        # 플레이어
            self.MLastspell.clip_draw(self.Lastframe1[self.Lastspelli], 120, self.Lastframe2[self.Lastspellj], 120, self.Player+250,self.All_Y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            player.stat = 10
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            player.stat = 40
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            player.stat += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            player.stat += 2
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            player.stat += 3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_f:
            player.stat += 4
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
