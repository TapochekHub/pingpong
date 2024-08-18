from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, speed, pic):
        super().__init__()
        self.image = transform.scale(image.load(pic),(width, height))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = pos_x
        self.rect.y = pos_y
        
    def reset(self):
        win.blit(self.image,  (self.rect.x, self.rect.y))

class Player(GameSprite):
    def player_1():
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y > 600:
            self.rect.y -= self.speed

    def player_2():
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y > 600:
            self.rect.y -= self.speed

biba = Player(30, 100, 100, 100, 4, "img/player.png")

boba = Player(30, 100, 800, 800, 4, "img/player.png")

ball = GameSprite(30, 30, 600, 600, 2, "img/ball.png")

win = display.set_mode((1280, 720))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("img/pp_bg.png"), (1920, 1080))





game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.blit(background, (0, 0))
    display.update()
    time.delay(60)

    biba.reset()
    biba.update()
    


    
