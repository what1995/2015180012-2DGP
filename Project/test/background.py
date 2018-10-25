from pico2d import *
import os

os.chdir('C:\\2DGP\\2015180012-2DGP\\Project\\FCGimage')
class BackGround:
    def __init__(self):
        self.image = load_image('Hakurei Shrine.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)
