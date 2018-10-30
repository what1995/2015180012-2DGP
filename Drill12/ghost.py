from pico2d import *
import game_framework
import random
import game_world
import math


PIXEL_PER_METER=(10.0/0.3)
RUN_SPEED_KMPH = 10
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS=(RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS=(RUN_SPEED_MPS*PIXEL_PER_METER)

TIME_PER_ACTION=0.5
ACTION_PER_TIME= 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION =8
# Boy Circle Speed
PIXEL_PER_SETA= math.pi/180
CIRCLE_SPEED_KMPH = 720*60*60
CIRCLE_SPEED_MPM = (CIRCLE_SPEED_KMPH/60.0)
CIRCLE_SPEED_MPS=(CIRCLE_SPEED_MPM/60.0)
CIRCLE_SPEED_PPS=(CIRCLE_SPEED_MPS*PIXEL_PER_SETA)


class Ghost:
    image = None

    def __init__(self, x = 400, y = 300):
        global cheak
        if Ghost.image == None:
            Ghost.image = load_image('animation_sheet.png')
        self.x, self.y= x, y
        self.frame = 0
        self.opacify=0
        self.set=0
        cheak=0

    def draw(self):
        global cheak

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        if cheak< 100:
            self.image.opacify(0.3)
            self.image.clip_draw(int(self.frame) * 100, 300, 100, 100, self.x,self.y+cheak)
            cheak +=RUN_SPEED_PPS* game_framework.frame_time
        else:
            self.image.opacify(self.opacify)
            self.image.clip_draw(int(self.frame) * 100, 300, 100, 100, self.x + 100 * math.sin(self.set),self.y + 100 * math.cos(self.set))

    def update(self):
        self.set += CIRCLE_SPEED_PPS *game_framework.frame_time
        self.opacify = random.randrange(1,10)*0.1

