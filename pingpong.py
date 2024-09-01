from pygame import *
import pygame_menu
font.init()
init()
font1 = font.SysFont("Arial", 120)
lose1 = font1.render("Player 1 lose!", True, (242, 230, 234))
lose2 = font1.render("Player 2 lose!", True, (242, 230, 234))
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
    def player_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 600:
            self.rect.y += self.speed

    def player_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed
def main():
    biba = Player(20, 120, 100, 100, 15, "img/player.png")

    boba = Player(20, 120, 1150, 100, 15, "img/player.png")

    ball = GameSprite(30, 30, 600, 600, 2, "img/ball.png")

    win = display.set_mode((1280, 720))
    display.set_caption("Пинг-понг")
    background = transform.scale(image.load("img/pp_bg.png"), (1920, 1080))

    speed_x = 5
    speed_y = 5


    finish = False
    while True:
        for e in event.get():
            if e.type == QUIT:
                return
        if finish != True:
            win.blit(background, (0, 0))
            biba.reset()
            biba.player_1()
            boba.reset()
            boba.player_2()
            ball.reset()


            ball.rect.x += speed_x
            ball.rect.y += speed_y

            if ball.rect.y < 0 or ball.rect.y > 690:
                speed_y = speed_y * -1

            if sprite.collide_rect(biba, ball) or sprite.collide_rect(boba, ball):
                speed_x = speed_x + 1
                speed_y = speed_y + 1
                speed_x = speed_x * -1
        if ball.rect.x < 0:
            finish = True
            win.blit(lose1, (80, 80))
            
        if ball.rect.x > 1220:
            finish = True
            win.blit(lose2, (80, 80))
            
        display.update()
        time.delay(60)
    
    
def start_menu():
    menu = pygame_menu.Menu("pingpong", 1280, 720, theme = pygame_menu.themes.THEME_DARK)
    menu.add.button("Начать", main)
    menu.add.button("Выйти", pygame_menu.events.EXIT)
    menu.mainloop(win)
    



start_menu()

    
