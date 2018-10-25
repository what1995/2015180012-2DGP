from pico2d import *
import os

os.chdir('C:\\2DGP\\2015180012-2DGP\\Project\\FCGimage')
class BackGround:
    def __init__(self):
        self.Shrine = load_image('Hakurei Shrine.png')
        self.clock = load_image('clock tower.png')
        self.bamboo = load_image('bamboo.png')
        self.center =load_image('center.png')

    def update(self):
        pass

    def draw(self):
        self.Shrine.draw(400, 300)
        self.center.draw(400, 500)
