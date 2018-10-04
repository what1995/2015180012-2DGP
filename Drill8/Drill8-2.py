from pico2d import *
import random
open_canvas()
KPU_WIDTH, KPU_HEIGHT = 800, 600
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')


def character_stam():
    global c
    if (c > 9):
        c = 9
    for j in range(0, c + 1):
        positon = points[j]
        character.clip_draw(100, 100, 100, 100, positon[0], positon[1])
def character_draw(p1, p2,p3, p4):
    frame = 0
    dir = 1
    global c
    if ((p2[0] - p1[0]) > 0):
        dir = -1
    elif ((p2[0] - p1[0]) < 0):
        dir = 1




    for i in range(0, 100, 10):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character_stam()

        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2

        if (dir == -1):
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        if (dir == 1):
            character.clip_draw(frame * 100, 0, 100, 100, x, y)


        update_canvas()
        frame = (frame + 1) % 8
        delay(0.1)





















size = 10
points =[(random.randint(0, 800), random.randint(0, 600)) for i in range(size)]
n=3
c=0
cheak=0
while True:
    character_draw(points[n - 3], points[n-2],points[n-1],points[n])

    n = (n + 1) % size
    c=c+1

close_canvas()