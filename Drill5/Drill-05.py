from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def character_1st_move():
     x1, y1=203, 535
     x2, y2=132, 243
     dir = 0
     if ((x2 - x1) > 0):
         dir = -1
     elif ((x2 - x1) < 0):
         dir = 1
     i=0
     frame=0
     move_x = (x2 - x1) / 10
     move_y = (y2 - y1) / 10
     while i < 10:
         clear_canvas()

         grass.draw(400, 30)
         if (dir == -1):
             character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
         if (dir == 1):
             character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
         update_canvas()
         frame = (frame + 1) % 8
         x1 = x1 + move_x
         y1 = y1 + move_y
         i +=1
         delay(0.1)



def character_2nd_move():
    x1, y1 = 132, 243
    x2, y2 = 535, 470
    dir = True
    if ((x2 - x1) > 0):
        dir = -1
    elif ((x2 - x1) < 0):
        dir = 1
    i = 0
    frame = 0
    move_x = (x2 - x1) / 10
    move_y = (y2 - y1) / 10
    while i < 10:
        clear_canvas()

        grass.draw(400, 30)
        if (dir == -1):
            character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        if (dir == 1):
            character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 = x1 + move_x
        y1 = y1 + move_y
        i += 1
        delay(0.1)
def character_3rd_move():
    x1, y1 = 535, 470
    x2, y2 = 477, 203
    dir = True
    if ((x2 - x1) > 0):
        dir = -1
    elif ((x2 - x1) < 0):
        dir = 1
    i = 0
    frame = 0
    move_x = (x2 - x1) / 10
    move_y = (y2 - y1) / 10
    while i < 10:
        clear_canvas()

        grass.draw(400, 30)
        if (dir == -1):
            character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        if (dir == 1):
            character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 = x1 + move_x
        y1 = y1 + move_y
        i += 1
        delay(0.1)
def character_4th_move():
    x1, y1 = 477, 203
    x2, y2 = 715, 136
    dir = True
    if ((x2 - x1) > 0):
        dir = -1
    elif ((x2 - x1) < 0):
        dir = 1
    i = 0
    frame = 0
    move_x = (x2 - x1) / 10
    move_y = (y2 - y1) / 10
    while i < 10:
        clear_canvas()

        grass.draw(400, 30)
        if (dir == -1):
            character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        if (dir == 1):
            character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 = x1 + move_x
        y1 = y1 + move_y
        i += 1
        delay(0.1)
def character_5th_move():
    x1, y1 = 715, 136
    x2, y2 = 316, 225
    dir = True
    if ((x2 - x1) > 0):
        dir = -1
    elif ((x2 - x1) < 0):
        dir = 1
    i = 0
    frame = 0
    move_x = (x2 - x1) / 10
    move_y = (y2 - y1) / 10
    while i < 10:
        clear_canvas()

        grass.draw(400, 30)
        if (dir == -1):
            character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        if (dir == 1):
            character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 = x1 + move_x
        y1 = y1 + move_y
        i += 1
        delay(0.1)
def character_6th_move():
    x1, y1 = 316, 225
    x2, y2 = 510, 92
    dir = True
    if ((x2 - x1) > 0):
        dir = -1
    elif ((x2 - x1) < 0):
        dir = 1
    i = 0
    frame = 0
    move_x = (x2 - x1) / 10
    move_y = (y2 - y1) / 10
    while i < 10:
        clear_canvas()

        grass.draw(400, 30)
        if (dir == -1):
            character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        if (dir == 1):
            character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 = x1 + move_x
        y1 = y1 + move_y
        i += 1
        delay(0.1)
def character_7th_move():
    x1, y1 = 510, 92
    x2, y2 = 692, 518
    dir = True
    if ((x2 - x1) > 0):
        dir = -1
    elif ((x2 - x1) < 0):
        dir = 1
    i = 0
    frame = 0
    move_x = (x2 - x1) / 10
    move_y = (y2 - y1) / 10
    while i < 10:
        clear_canvas()

        grass.draw(400, 30)
        if (dir == -1):
            character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        if (dir == 1):
            character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 = x1 + move_x
        y1 = y1 + move_y
        i += 1
        delay(0.1)
def character_8th_move():
    x1, y1 = 692, 518
    x2, y2 = 682, 336
    dir = True
    if ((x2 - x1) > 0):
        dir = -1
    elif ((x2 - x1) < 0):
        dir = 1
    i = 0
    frame = 0
    move_x = (x2 - x1) / 10
    move_y = (y2 - y1) / 10
    while i < 10:
        clear_canvas()

        grass.draw(400, 30)
        if (dir == -1):
            character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        if (dir == 1):
            character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 = x1 + move_x
        y1 = y1 + move_y
        i += 1
        delay(0.1)
def character_9th_move():
    x1, y1 = 682, 336
    x2, y2 = 712, 349
    dir = True
    if ((x2 - x1) > 0):
        dir = -1
    elif ((x2 - x1) < 0):
        dir = 1
    i = 0
    frame = 0
    move_x = (x2 - x1) / 10
    move_y = (y2 - y1) / 10
    while i < 10:
        clear_canvas()

        grass.draw(400, 30)
        if (dir == -1):
            character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        if (dir == 1):
            character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 = x1 + move_x
        y1 = y1 + move_y
        i += 1
        delay(0.1)
def character_10th_move():
    x1, y1 = 712, 349
    x2, y2 = 203, 535
    dir = True
    if ((x2 - x1) > 0):
        dir = -1
    elif ((x2 - x1) < 0):
        dir = 1
    i = 0
    frame = 0
    move_x = (x2 - x1) / 10
    move_y = (y2 - y1) / 10
    while i < 10:
        clear_canvas()

        grass.draw(400, 30)
        if (dir == -1):
            character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        if (dir == 1):
            character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 = x1 + move_x
        y1 = y1 + move_y
        i += 1
        delay(0.1)
while True:
    character_1st_move()
    character_2nd_move()
    character_3rd_move()
    character_4th_move()
    character_5th_move()
    character_6th_move()
    character_7th_move()
    character_8th_move()
    character_9th_move()
    character_10th_move()

close_canvas()
