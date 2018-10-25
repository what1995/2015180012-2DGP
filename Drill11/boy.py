from pico2d import *

# Boy Event
# fill here
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP ,LSHIFT_DOWN,LSHIFT_UP,RSHIFT_DOWN,RSHIFT_UP= range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_LSHIFT): LSHIFT_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): LSHIFT_UP,
    (SDL_KEYDOWN, SDLK_RSHIFT): RSHIFT_DOWN,
    (SDL_KEYUP, SDLK_RSHIFT): RSHIFT_UP
}



# Boy States
class IdleState:
    @staticmethod
    def enter(boy):
        boy.frame=0
        boy.timer=1000

    @staticmethod
    def exit(boy):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame+1)%8

    @staticmethod
    def draw(boy):
        if boy.dir ==1:
            boy.image.clip_draw(boy.frame*100,300,100,100,boy.x,boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)


class RunState:
    @staticmethod
    def enter(boy):
        boy.frame=0
        boy.dir = boy.velocity

    @staticmethod
    def exit(boy):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.x += boy.velocity
        boy.x= clamp(25,boy.x,800-25)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


# fill here

class DashState:
    @staticmethod
    def enter(boy):
        boy.speed=5
        boy.frame = 0
        boy.time=0
        boy.dir = boy.velocity

    @staticmethod
    def exit(boy):
        pass
    @staticmethod
    def do(boy):

        boy.frame = (boy.frame + 1) % 8
        boy.time =(boy.time +1)%30
        if(boy.time==0):
            boy.speed=1
        boy.x += boy.velocity*boy.speed
        boy.x = clamp(25, boy.x, 800 - 25)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


next_state_table = {
    IdleState: {RIGHT_UP:RunState,LEFT_UP:RunState,RIGHT_DOWN:RunState,LEFT_DOWN:RunState,RSHIFT_DOWN:IdleState,RSHIFT_UP:IdleState,LSHIFT_DOWN:IdleState,LSHIFT_UP:IdleState},
    RunState:{RIGHT_UP:IdleState,LEFT_UP:IdleState,LEFT_DOWN:IdleState,RIGHT_DOWN:IdleState,RSHIFT_DOWN:DashState,RSHIFT_UP:RunState,LSHIFT_DOWN:DashState,LSHIFT_UP:RunState},
    DashState:{RIGHT_UP:IdleState,LEFT_UP:IdleState,LEFT_DOWN:IdleState,RIGHT_DOWN:IdleState,RSHIFT_DOWN:RunState,RSHIFT_UP:RunState,LSHIFT_DOWN:RunState,LSHIFT_UP:RunState}
# fill here
}







class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        #self.speed=1
        self.event_que = []
        self.cur_state=IdleState
        self.cur_state.enter(self)
        # fill here
        pass


    def change_state(self,  state):
        self.cur_state.exit(self)
        self.cur_state = state
        self.cur_state.enter(self)
        # fill here



    def add_event(self, event):
        self.event_que.insert(0,event)


    def update(self):
        self.cur_state.do(self)
        if len(self.event_que)>0:
            event=self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])




    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if(event.type,event.key) in key_event_table:
            key_event = key_event_table[(event.type,event.key)]
            if key_event ==RIGHT_DOWN:
                self.velocity +=1
            elif key_event ==LEFT_DOWN:
                self.velocity -=1
            elif key_event == RIGHT_UP:
                self.velocity -=1
            elif key_event==LEFT_UP:
                self.velocity +=1

            self.add_event(key_event)

