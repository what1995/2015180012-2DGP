from pico2d import *
import random
open_canvas()
KPU_WIDTH, KPU_HEIGHT = 800, 600
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')



def character_draw(p1, p2,p3, p4):
    




    pass

















size = 10
points =[(random.randint(0, 800), random.randint(0, 600)) for i in range(size)]
n=3
while True:
    character_draw(points[n - 3], points[n-2],points[n-1],points[n])
    n = (n + 1) % size

close_canvas()