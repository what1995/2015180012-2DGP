from pico2d import *

class BackGround:
    def __init__(self):
        self.image = load_image('Hakurei Shrine.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)
