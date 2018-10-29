from pico2d import *
import os

os.chdir('C:\\2DGP\\2015180012-2DGP\\Project\\FCGimage')
import iku
attack=None
class Enemy_HP:
    def __init__(self):

        self.x = 600
        self.y = 500
        self.damage = 0
        self.Power = 1
        self.HPBar = load_image('HP-Damege.png')
        self.HP = load_image('HP-HP.png')

    def update(self):
        global attack
        attack = iku.HP
        if self.Power < attack:
            self.damage -= 4
            self.Power += 1

    def draw(self):
        self.HPBar.draw(self.x, self.y)
        self.HP.clip_draw(0, 0,252+self.damage,15,self.x+(self.damage//2),self.y)

