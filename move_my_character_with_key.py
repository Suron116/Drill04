from pico2d import *

open_canvas(1280, 1024)

back = load_image('TUK_GROUND.png')
#back.draw_now(640, 512)

character = load_image('sprite_sheet.png')

def handle_events():
    global moving
    global char_x
    global char_y
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            moving = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                if char_x < 1280:
                    char_x += 10
                dir = 0
            elif event.key == SDLK_LEFT:
                if char_x > 10:
                    char_x -= 10
                dir = 600
            elif event.key == SDLK_UP:
                if char_y < 1000:
                    char_y += 10
                dir = 1200
            elif event.key == SDLK_DOWN:
                if char_y > 50:
                    char_y -= 10
                dir = 1800
            elif event.key == SDLK_ESCAPE:
                moving = False

moving = True
char_x, char_y, dir = 640, 512, 0
frame = 0

#캐릭터 이미지 길이
while moving:
    clear_canvas()
    back.draw_now(640, 512)
    character.clip_draw(frame * 100, dir, 800, 550, char_x, char_y, 150, 100)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)