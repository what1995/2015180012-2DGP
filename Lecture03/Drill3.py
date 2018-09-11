from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
x=400
y=90
shape=1
C=0
while (1):
    
    if(shape==1):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+2
        if(x==780):
            shape=2
        delay(0.001)
    elif(shape==2):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y+2
        if(y==560):
            shape=3
        delay(0.001)
    elif(shape==3):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-2
        if(x==20):
            shape=4
        delay(0.001)
    elif(shape==4):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-2
        if(y==90):
            shape=5
        delay(0.001)
    elif(shape==5):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+2
        if(x==400):
            shape=6
        delay(0.001)
    elif(shape==6):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x+400*math.sin(math.radians(C)),(y*3)-200*math.cos(math.radians(C)))
        C=C+2
        delay(0.01)
        if(C==360):
            shape=1
            C=0




    

close_canvas()
