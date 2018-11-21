import random
from pico2d import *
import game_world
import game_framework

import boy
class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball41x41.png')
            self.canvas_width = get_canvas_width()
            self.canvas_height = get_canvas_height()
        self.x, self.y, self.fall_speed = random.randint(0,2400), random.randint(0, 2400), 0

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

