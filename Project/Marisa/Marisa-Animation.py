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
        self.Damage = load_image('MarisaDamage-Motion.png')
        self.Down = load_image('MarisaDown-Motion.png')
        self.Skill1 = load_image('MarisaSkill1-Motion.png')
        self.S1Effect = load_image('MarisaSkill1.png')
        self.Skill2 = load_image('MarisaSkill2-Motion.png')
        self.S2Effect = load_image('MarisaSkill2.png')
        self.Skill3 = load_image('MarisaSkill3-Motion.png')
        self.S3Effect = load_image('MarisaSKill3.png')
        self.Lastspell = load_image('MarisaLastspell-Motion.png')
        self.LastspellEffect = load_image('MarisaLastspell.png')
        self.Standing = load_image('MarisaStanding-Motion.png')

    def update(self):
        pass
    def Damage(self):
        pass




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
running=True

while running:
    handle_events()
    clear_canvas()
    background.draw()
    update_canvas()
    delay(0.05)
# finalization code
close_canvas()