from pico2d import *
import random

class Grass:
    def __init__(self):

        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 500
        self.image = load_image('ball41x41.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 500
        self.image = load_image('ball21x21.png')

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
small=SmallBall()
running = True

# game main loop code
while running:
    handle_events()

    clear_canvas()
    grass.draw()
    big.draw()
    small.draw()
    update_canvas()

    delay(0.05)
# finalization code
close_canvas()