#Создай собственный Шутер!

from pygame import *
from random import randint
font.init()
win_widht = 700
win_height = 500
window = display.set_mode(
    (win_widht, win_height)
)
mixer.init()
mixer.music.load('space.ogg')
fire_sound = mixer.Sound('fire.ogg')
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
background = transform.scale(
  image.load("galaxy.jpg"),(700,500)
)
lost=0
font2 = font.Font(None, 30)
bullets = sprite.Group()
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a]and x1>=5:
            self.rect.x -=10
        if keys_pressed[K_d]and x1<=620:
            self.rect.x +=10
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 25, 15, 15)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y +=10
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80, 620)
            self.rect.y = 0
            lost +=1
        if self.rect.y >500:
            self.rect.y = -20
            self.rect.x = randint(50,650)
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <-10:
            self.kill()
monster = Enemy("ufo.png",randint(50,650),0,5,65,65)
monsters = sprite.Group()
monsters.add(monster)
x1=350
player = Player("rocket.png",x1,400,15,65,65)
game = True
FPS = 60
finish = False
clock = time.Clock()
mixer.music.play()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                player.fire()
    if finish != True:
        window.blit(background,(0, 0))
        monsters.draw(window)
        bullets.draw(window)
        text_lose = font2.render("Пропущено:" + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10,10))
        text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        monsters.update()
        bullets.update()
        player.update()
        player.reset()
        display.update()
        clock.tick(FPS)