from pico2d import *
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
Mouse = load_image('hand_arrow.png')

running = True
x = 0
frame = 0


def handle_events():
    # fill here
    pass


while x < 800 and running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)

close_canvas()
