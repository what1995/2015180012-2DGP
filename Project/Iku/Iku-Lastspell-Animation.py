from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
IkuLastspell = load_image('IkuLastspell-Motion.png')


def Iku_Lastspell():
        frame1 = [60,60,60,63,72,125,130,130,125]
        frame2 = [0,60,120,180,243,315,440,570,700,825,945,1035]
        cheak=0
        i=0
        j=0
        while(cheak<9):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                IkuLastspell.clip_draw(frame2[i],0,frame1[j],140,Enemy_X,All_Y)
                #플레이어
                IkuLastspell.clip_draw(frame2[i],140,frame1[j],140,Player_X,All_Y)
                i=(i+1)%10
                j=(j+1)%9
                update_canvas()
                delay(0.5)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Iku_Lastspell()


close_canvas()
        
