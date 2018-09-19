from pico2d import *
KPU_WIDTH, KPU_HEIGHT = 800, 600




running = True
x = 0
frame = 0


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running = False
        elif event.type ==SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT -1 - event.y
        elif event.type==SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
Mouse = load_image('hand_arrow.png')

while x < KPU_WIDTH and running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH//2, KPU_HEIGHT//2)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)

close_canvas()
