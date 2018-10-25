from pico2d import *

import game_world

# Boy Event
RIGHT_DOWN, LEFT_DOWN,Stand = range(3)

key_event_table = {
    #(SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
(SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN
}


# Boy States

class StandState:

    @staticmethod
    def enter(iku, event):
        iku.motion = 0
        iku.frame1 = 0
        iku.frame2 = 0
        iku.Standframe1 = [0, 73, 140, 200, 265, 324, 385, 446, 510, 580]
        iku.Standframe2 = [74, 64, 60, 62, 58, 59, 63, 65, 70]
        if event == RIGHT_DOWN:
            iku.motion = 1
        if event == LEFT_DOWN:
            iku.motion = 2
            iku.timer = 300

    @staticmethod
    def exit(iku, event):
        pass
    @staticmethod
    def do(iku):
        iku.frame1 = (iku.frame1 + 1) % 9
        iku.frame2 = (iku.frame2 + 1) % 9
        delay(0.1)
        iku.timer -= 1


    @staticmethod
    def draw(iku):
        if iku.motion ==0:
            iku.stand.clip_draw(iku.Standframe1[iku.frame1], 130, iku.Standframe2[iku.frame2], 130, iku.x, iku.y)


class Skill1State:

    @staticmethod
    def enter(boy, event):
        boy.frame1 = 0
        boy.frame2 = 0
        boy.S1frame = 0
        boy.Skill1Eframe1 = 0
        boy.skill1cheak = 0
        boy.Skill1frame1 = [0, 68, 133, 193, 259, 329, 390, 470, 543, 615, 680, 745]
        boy.Skill1frame2 = [68, 65, 60, 66, 68, 59, 78, 74, 70, 63, 68]
        if event == RIGHT_DOWN:
            boy.motion = 1


    @staticmethod
    def exit(boy, event):
        pass
        #if event ==SPACE:
        #    boy.fire_ball()
    @staticmethod
    def do(boy):
        if boy.skill1cheak<8:
            boy.frame1 = (boy.frame1 + 1) % 11
            boy.frame2 = (boy.frame2 + 1) % 11
        if boy.skill1cheak>=8 and boy.skill1cheak<20:
            boy.S1frame = (boy.S1frame + 1) % 12
            boy.Skill1Eframe1 = (boy.Skill1Eframe1 + 1) % 7
        if boy.skill1cheak>=20:
            boy.frame1 = (boy.frame1 + 1) % 11
            boy.frame2 = (boy.frame2 + 1) % 11
        boy.skill1cheak +=1
        if  boy.skill1cheak==23:
            boy.skill1cheak=0

            boy.add_event(Stand)
        delay(0.1)

    @staticmethod
    def draw(boy):
        if boy.motion == 1:
            boy.skill1.clip_draw(boy.Skill1frame1[boy.frame1], 145, boy.Skill1frame2[boy.frame2], 145, boy.x, boy.y)
            if boy.skill1cheak >= 8 and boy.skill1cheak < 20:
                boy.S1effect.clip_draw(0, boy.S1frame * 52, 360, 52, boy.x + 200, boy.y + 10)
                boy.S1effect2.clip_draw(boy.Skill1Eframe1 * 65, 0, 68, 60,boy.x + 400, boy.y + 10)


class Skill2State:
    @staticmethod
    def enter(boy,event):
        boy.frame1 = 0
        boy.frame2 = 0
        boy.S2frame = 0
        boy.Skill2Eframe1 = 0
        boy.skill2cheak = 0
        boy.skill2Px = 300
        boy.skill2Mx = 330
        boy.Skill2frame1 = [0, 70, 130, 200, 283, 356, 422, 490, 597, 732, 912, 1087, 1247, 1375, 1463, 1520]
        boy.Skill2frame2 = [70, 60, 70, 83, 73, 66, 66, 101, 133, 178, 173, 157, 124, 83, 63]
        if event == LEFT_DOWN:
            boy.motion = 2

    @staticmethod
    def exit(boy,event):
        pass
    @staticmethod
    def do(boy):
        if boy.skill2cheak < 19:
            if boy.skill2cheak < 11:
                boy.frame1 = (boy.frame1 + 1) % 16
                boy.frame2 = (boy.frame2 + 1) % 15
            if boy.skill2cheak > 5 and boy.skill2cheak < 15:
                if boy.skill2cheak > 8:
                    boy.skill2Mx += 10
                    boy.skill2Px += 10
            if boy.skill2cheak >= 15:
                boy.frame1 = (boy.frame1 + 1) % 16
                boy.frame2 = (boy.frame2 + 1) % 15
                boy.skill2Px -= 10
                boy.Skill2Eframe1 = (boy.Skill2Eframe1 + 1) % 6
            boy.skill2cheak += 1
        if boy.skill2cheak == 19:
            boy.skill2cheak = 0
            boy.add_event(Stand)
        delay(0.1)

    @staticmethod
    def draw(boy):
        if boy.motion == 2:
            boy.skill2.clip_draw(boy.Skill2frame1[boy.frame1], 145, boy.Skill2frame2[boy.frame2], 145,boy.x+boy.skill2Px, boy.y)
            if boy.skill2cheak > 5 and boy.skill2cheak < 15:
                boy.S2effect.clip_draw(boy.S2frame * 193, 60, 193, 60, boy.x + boy.skill2Mx, boy.y - 5)

class DashState:
    @staticmethod
    def enter(boy,event):
        boy.frame = 0
        boy.time = 0
        boy.speed = 5


    @staticmethod
    def exit(boy,event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.time = (boy.time + 1) % 75
        if boy.time ==0:
            boy.speed = 1
        boy.x += boy.velocity * boy.speed
        boy.x = clamp(25, boy.x, 1600 - 25)
    @staticmethod
    def draw(boy):
        if boy.motion == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)



next_state_table = {
    StandState: {RIGHT_DOWN: Skill1State, LEFT_DOWN: Skill2State},
    Skill1State: {RIGHT_DOWN: StandState,LEFT_DOWN: Skill1State,Stand:StandState},
    Skill2State:{ RIGHT_DOWN: Skill2State, LEFT_DOWN: StandState,Stand:StandState},
    DashState:{LEFT_DOWN:StandState,RIGHT_DOWN:StandState}

}

class Iku:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.stand = load_image('Iku-Standing-Motion.png')

        self.skill1 = load_image('IkuSkill1-Motion.png')
        self.S1effect = load_image('IkuSkill1-1.png')
        self.S1effect2 = load_image('IkuSkill1-2.png')

        self.skill2 = load_image('IkuSkill2-Motion.png')
        self.S2effect = load_image('IkuSkill2-1.png')

        self.dir = 1
        self.motion = 0
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = StandState
        self.cur_state.enter(self, None)





    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.button) in key_event_table:
            key_event = key_event_table[(event.type, event.button)]
            self.add_event(key_event)
        elif (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

