from pico2d import *
import random
open_canvas()
KPU_WIDTH, KPU_HEIGHT = 800, 600
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')

def character_draw(p1, p2):
    frame =0
    dir =0

    

    for i in range(0, 100, 10):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH//2, KPU_HEIGHT//2)
        t= i/100
        x= (1-t)*p1[0]+t*p2[0]
        y= (1-t)*p1[1]+t*p2[1]

        update_canvas()

        delay(0.1)

size = 20
points =[(random.randint(0, 800), random.randint(0, 600)) for i in range(size)]

n = 1
while True:

    character_draw(points[n-1], points[n])
    n = (n+1) % size


close_canvas()



