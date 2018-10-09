from pico2d import *
import random
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.frame =random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame+1)%8
        self.x +=5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Grass:
    def __init__(self):

        self.image = load_image('grass.png')


    def draw(self):
        self.image.draw(400, 30)

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.speed = random.randint(10, 30)
        self.image = load_image('ball41x41.png')
    def update(self):
        if(self.y>90-20):
            self.y -= self.speed
    def draw(self):
        self.image.draw(self.x, self.y)

class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.speed = random.randint(10, 30)
        self.image = load_image('ball21x21.png')
    def update(self):
        if(self.y>90-20):
            self.y -= self.speed
    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
grass = Grass()
big = BigBall()
team = [Boy() for i in range(11)]
small=SmallBall()
running = True

smallcheak = random.randint(1, 20)
bigcheak = 20 - smallcheak

smallteam = [SmallBall() for i in range(smallcheak)]
bigteam = [BigBall() for j in range(bigcheak)]
# game main loop code
while running:
    handle_events()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
        boy.update()

    for big in bigteam:
        big.draw()
        big.update()
    for small in smallteam:
        small.draw()
        small.update()
    update_canvas()

    delay(0.05)
# finalization code
close_canvas()