from pico2d import *
KPU_WIDTH, KPU_HEIGHT = 800, 600



moving = True
running = True
M_x = 0
M_y = 0
C_x = KPU_WIDTH//2
C_y = KPU_HEIGHT//2
C_M_x = 0
C_M_y = 0
frame = 0
dir = 1
cheak=0

def handle_events():
    global running
    global M_x, M_y
    global C_x, C_y
    global C_M_x, C_M_y
    global moving
    global cheak
    global dir
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running = False
        elif event.type ==SDL_MOUSEMOTION:
            M_x, M_y = event.x +35, KPU_HEIGHT - event.y -35
        elif event.type==SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            running = False
        elif event.type==SDL_MOUSEBUTTONDOWN:
            moving=True
            cheak=0
            if (event.x - C_x)>0:
                dir = -1
            elif (event.x - C_x)<0:
                dir = 1
            C_M_x, C_M_y = (event.x - C_x) / 10, (KPU_HEIGHT - event.y - C_y) / 10









open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
Mouse = load_image('hand_arrow.png')

while M_x < KPU_WIDTH and running:
    clear_canvas()
    hide_cursor()
    kpu_ground.draw(KPU_WIDTH//2, KPU_HEIGHT//2)
    Mouse.clip_draw(0, 0, 100, 100, M_x, M_y)
    if (dir == -1):
        character.clip_draw(frame * 100, 100, 100, 100, C_x, C_y)
    if (dir == 1):
        character.clip_draw(frame * 100, 0, 100, 100, C_x, C_y)
    frame = (frame + 1) % 8
    if moving == True:
        C_x += C_M_x
        C_y += C_M_y
        cheak = cheak + 1
    if cheak ==10:
        moving=False
        cheak=0



    update_canvas()


    handle_events()
    delay(0.05)


close_canvas()
