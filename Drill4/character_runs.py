from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
cheak = 0
frame = 0

while(1):
    if (cheak ==0):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame *100,100,100,100,x,90)
        update_canvas()
        frame=(frame+1)%8
        x +=10
        if(x>=800):
            cheak=1
        
        delay(0.05)
        get_events()
    if (cheak==1):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame *100,0,100,100,x,90)
        update_canvas()
        frame=(frame+1)%8
        x -=10
        if(x<=0):
            cheak=0
        delay(0.05)
        get_events()


close_canvas()

