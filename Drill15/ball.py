import random
from pico2d import *
import game_world
import game_framework

import boy
class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
            self.canvas_width = get_canvas_width()
            self.canvas_height = get_canvas_height()
        self.x, self.y, self.fall_speed = random.randint(0,1840), random.randint(0, 1110), 0

    def get_bb(self):
        global cx,cy
        return cx - 10, cy - 10, cx + 10, cy + 10


    def draw(self):
        global cx,cy
        cx = self.x - boy.window_left
        cy = self.y - boy.window_bottom
        self.image.draw(cx, cy)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

