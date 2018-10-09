from pico2d import *


class BackGround:
    def __init__(self):
        self.x, self.y = 400, 300
        self.Shrine = load_image('Hakurei Shrine.png')

    def draw(self):
        self.Shrine.draw(self.x,self.y)

class Marisa:
    def __init__(self):
        self.Player = 200
        self.Enemy =600
        self.All_Y=200

        self.Dmage = load_image('MarisaDamage-Motion.png')
        self.Dmagei = 0
        self.Dmagej = 0
        self.Dmagecheak = 0

        self.Down = load_image('MarisaDown-Motion.png')
        self.Downi = 0
        self.Downj = 0
        self.Downcheak = 0

        self.Skill1 = load_image('MarisaSkill1-Motion.png')
        self.Skill1i =0
        self.Skill1j =0
        self.Skill1cheak=0
        self.S1Effect = load_image('MarisaSkill1.png')
        self.Skill1Ei = 0
        self.Skill1Ej = 0
        self.Skill1Eframe1 = 0





        self.Skill2 = load_image('MarisaSkill2-Motion.png')
        self.S2Effect = load_image('MarisaSkill2.png')
        self.Skill3 = load_image('MarisaSkill3-Motion.png')
        self.S3Effect = load_image('MarisaSKill3.png')
        self.Lastspell = load_image('MarisaLastspell-Motion.png')
        self.LastspellEffect = load_image('MarisaLastspell.png')
        self.Standing = load_image('MarisaStanding-Motion.png')
        self.Standi = 0
        self.Standj = 0
        self.Standcheak =0


    def update(self):
       pass


    def Damage(self):
        self.DamageFlame1 = [0, 90, 175, 240]
        self.DamageFlame2 = [90, 85, 65]
        #플레이어
        self.Dmage.clip_draw(self.DamageFlame1[self.Dmagei], 115, self.DamageFlame2[self.Dmagej],115,self.Player,self.All_Y)
        #적
        self.Dmage.clip_draw(self.DamageFlame1[self.Dmagei], 0, self.DamageFlame2[self.Dmagej], 115, self.Enemy, self.All_Y)
        if self.Dmagecheak <3:
            self.Dmagei = (self.Dmagei + 1) % 4
            self.Dmagej = (self.Dmagej + 1) % 3
            self.Dmagecheak += 1
        if self.Dmagecheak ==3:
            self.Dmagei = 0
            self.Dmagej = 0
            self.Dmagecheak=0

    def Downs(self):
        self.Downframe1 = [0,80,149,232,348,451,548,645]
        self.Downframe2 = [80,69,83,116,102,95,100]

        #플레이어
        self.Down.clip_draw(self.Downframe1[self.Downi], 95, self.Downframe2[self.Downj], 95, self.Player, self.All_Y-20)
        #적
        self.Down.clip_draw(self.Downframe1[self.Downi], 0, self.Downframe2[self.Downj], 95, self.Enemy, self.All_Y - 20)

        if self.Downcheak <7:
            self.Downi = (self.Downi + 1) % 8
            self.Downj = (self.Downj + 1) % 7
            self.Downcheak += 1
        if self.Downcheak ==7:
            self.Downi = 0
            self.Downj = 0
            self.Downcheak=0

    def Stand(self):
        self.Standframe1 = [0,65,126,188,250,312,372,434,495,556,618]
        self.Standframe2 = [65,61,62,62,62,60,62,61,60,62]
        #플레이어
        self.Standing.clip_draw(self.Standframe1[self.Standi], 110, self.Standframe2[self.Standj], 110, self.Player,self.All_Y )
        #적
        self.Standing.clip_draw(self.Standframe1[self.Standi], 0, self.Standframe2[self.Standj], 110, self.Enemy,self.All_Y)

        if self.Standcheak < 10:
            self.Standi = (self.Standi+1) % 11
            self.Standj = (self.Standj+1) % 10
            self.Standcheak += 1
        if self.Standcheak == 9:
            self.Standi = 0
            self.Standj= 0
            self.Standcheak = 0

    def MSkill1(self):
        self.Skill1frame1 =[0, 71, 132, 197, 262, 322, 396, 468, 536, 600]
        self.Skill1frame2 =[71,61,65,65,58,72,72,66,60]

        self.Skill1Eframe2=0
        #플레이어
        self.Skill1.clip_draw(self.Skill1frame1[self.Skill1i], 105, self.Skill1frame2[self.Skill1j], 105, self.Player,self.All_Y)
        #적
        self.Skill1.clip_draw(self.Skill1frame1[self.Skill1i], 0, self.Skill1frame2[self.Skill1j], 105, self.Enemy,self.All_Y)

        if self.Skill1cheak < 18:
            if self.Skill1cheak < 6:
                self.Skill1i = (self.Skill1i + 1) % 10
                self.Skill1j = (self.Skill1j + 1) % 9
            if self.Skill1cheak > 6:
                #Player
                self.S1Effect.clip_draw(self.Skill1Eframe1 * 260, 0, 260, 505, self.Enemy, self.All_Y+150)
                #Enemy
                self.S1Effect.clip_draw(self.Skill1Eframe1 * 260, 0, 260, 505, self.Player, self.All_Y + 150)
                if self.Skill1cheak < 15:
                    self.Skill1Eframe1 = (self.Skill1Eframe1 + 1) % 9
                if self.Skill1cheak >= 15:
                    self.Skill1i = (self.Skill1i + 1) % 10
                    self.Skill1j = (self.Skill1j + 1) % 9
            self.Skill1cheak += 1






        if self.Skill1cheak == 18:
            self.Skill1i =0
            self.Skill1j =0
            self.Skill1cheak=0
            self.Skill1Eframe1=0



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False




open_canvas()
background=BackGround()
marisa=Marisa()
running=True

while running:
    handle_events()
    clear_canvas()
    background.draw()
    marisa.update()
    #marisa.Damage()
    #marisa.Downs()
    #marisa.Stand()
    marisa.MSkill1()
    update_canvas()
    delay(0.1)
# finalization code
close_canvas()