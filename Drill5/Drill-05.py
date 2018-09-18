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
    pass
def character_4th_move():
    pass
def character_5th_move():
    pass
def character_6th_move():
    pass
def character_7th_move():
    pass
def character_8th_move():
    pass
def character_9th_move():
    pass
def character_10th_move():
    pass
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
