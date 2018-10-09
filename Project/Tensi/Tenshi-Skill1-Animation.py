from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200

TenshiSkill1 = load_image('TenshiSkill1-Motion.png')
TenshiSkill1effect = load_image('TenshiSkill1.png')


def Tenshi_Skill1():
        frame1 = [75,67,70,77,82,120,112,73,73,73,71,68,65,63,64]
        frame2 = [0,75,143,214,294,379,500,616,695,776,852,929,1006,1076,1146,1210]
        cheak=0
        i=0
        j=0
        Sy=160
        while(cheak<15):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                TenshiSkill1.clip_draw(frame2[i],0,frame1[j],160,Enemy_X,All_Y)
                #플레이어
                TenshiSkill1.clip_draw(frame2[i],160,frame1[j],160,Player_X,All_Y)
                i=(i+1)%16
                j=(j+1)%15
                if cheak >7:
                    TenshiSkill1effect.clip_draw(0,0,260,165,Enemy_X,All_Y+Sy)
                    Sy -= 30
                update_canvas()
                delay(0.13)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Tenshi_Skill1()


close_canvas()
        

