import game_framework
import pico2d
import os

os.chdir('C:\\2DGP\\2015180012-2DGP\\Project\\FCGimage')
import  FCG_title

pico2d.open_canvas()
game_framework.run(FCG_title)
pico2d.close_canvas()
