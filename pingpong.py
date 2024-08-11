from pygame import *

win = display.set_mode((1280, 720))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("pp_bg.png"), (1920, 1080))


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.blit(background, (0, 0))
    display.update()
    time.delay(60)
    
