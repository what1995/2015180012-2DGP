from pico2d import *
import game_framework
import random
import game_world
import math

TIME_PER_ACTION=0.5
ACTION_PER_TIME= 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION =8
# Boy Circle Speed
PIXEL_PER_METER=(10.0/0.3)
CIRCLE_SPEED_KMPH = 6
CIRCLE_SPEED_MPM = (CIRCLE_SPEED_KMPH/60.0)
CIRCLE_SPEED_MPS=(CIRCLE_SPEED_MPM/60.0)
CIRCLE_SPEED_PPS=(CIRCLE_SPEED_MPS*PIXEL_PER_METER)


class Ghost:
    image = None

    def __init__(self, x = 400, y = 300):
        if Ghost.image == None:
            Ghost.image = load_image('animation_sheet.png')
        self.x, self.y= x, y
        self.frame = 0
        self.opacify=0
        self.set=0

    def draw(self):
        self.image.opacify(0.5)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.image.clip_draw(int(self.frame) * 100, 300, 100, 100, self.x + 100 * math.sin(self.set),self.y + 100 * math.cos(self.set))

    def update(self):
        self.set += CIRCLE_SPEED_PPS

