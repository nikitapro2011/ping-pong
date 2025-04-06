from pygame import *
from random import randint
# from time import time as timer
# from random import randint 
# mixer.init()
window = display.set_mode((700, 500))
display.set_caption('Danger пин понг')
background = transform.scale(image.load('backside.png'), (700, 500))
# window.fill((10,4,80))
clock = time.Clock()
FPS = 60
keys_pressed = key.get_pressed()
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

ball = GameSprite('ball.png', 300, 300, 3, 40, 40)



class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > -5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < 300:
            self.rect.y += self.speed
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > -5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed
plat = Player('platform.png', 10, 250, 5, 10, 200)
plat2 = Player('platform1.png', 670, 250, 5, 10, 200)

# lost = 0
# class Enemy(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > 500:
#             self.rect.y = 0
#             self.rect.x = randint(50,650)
#             lost = lost + 1

# class Bullet(GameSprite):
#     def update(self):
#         self.rect.y -= self.speed
#         if self.rect.y < 0:
#             self.kill()

# bullets = sprite.Group()
# monsters = sprite.Group()
# sters = sprite.Group()
# for i in range(10):
#     monster = Enemy('ufo.png', randint(50,650), -40, 2, 80, 50)
#     monsters.add(monster)
# for i in range(2):
#     ster = Enemy('asteroid.png', randint(50,650), -40, 2, 80, 50)
#     sters.add(ster)

# finish = False
# rel_time = False 
# font.init()
# font2 = font.SysFont('Arial', 40)
# score = 0
# font1 = font.SysFont('Arial', 80)
# win = font1.render('YOU WIN!', True, (255, 255, 255))
# lose = font1.render('YOU LOSE!', True, (180, 0, 0))
# num_fire = 0

# while game:
#     for e in event.get():
#         if e.type == QUIT:
#             game = False
#         elif e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 # fire.play()
#                 bullet = Bullet('bullet.png', 5, 400, 9, 10, 10)
#                 bullets.add(bullet)
#                 if num_fire < 5 and rel_time == False:
#                     num_fire = num_fire + 1
#                     # fire.play()
#                     rock.fire()

#                 if num_fire >= 5 and rel_time == False:
#                     lost_time = timer()
#                     rel_time = True
                
#     if finish != True:
#         text_lose = font2.render('Пропущено:' + str(lost), 1, (255, 255, 255))
#         text_kill = font2.render('Убито:' + str(score), 1, (255, 255, 255))
#         window.blit(background,(0, 0))
#         window.blit(text_lose, (10, 20))
#         window.blit(text_kill, (10, 40))
#         rock.update()
#         rock.reset()
#         ster.update()
#         ster.reset()
#         monsters.draw(window)
#         monsters.update()
#         bullets.draw(window)
#         bullets.update()
#         collides = sprite.groupcollide(monsters, bullets, True, True)
#         for c in collides:
#             score = score + 1
#             # monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
#             monster = Enemy('ufo.png', randint(50,650), -40, 2, 80, 50)
#             monsters.add(monster)
    
#         if sprite.spritecollide(rock, monsters, False) or lost >= 3:
#             finish = True
#             window.blit(lose, (200, 200))
    
#         if score >= 10:
#             finish = True
#             window.blit(win, (200, 200))
#         if rel_time == True:
#             now_time = timer()
#             if now_time - lost_time < 3:
#                 reload = font2.render('wait, reload...', 1, (150, 0, 0))
#                 window.blit(reload, (260, 460)) 
#             else:
#                 num_fire = 0
#                 rel_time = False
        
#     else:
#         finish = False
#         score = 0
#         lost = 0
#         for b in bullets:
#             b.kill()
#         for m in monsters:
#             m.kill()
#         time.delay(3000)
#         for i in range(1, 6):
#             monster = Enemy('ufo.png', randint(50,650), -40, 2, 80, 50)
#             monsters.add(monster)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0, 0))
    ball.update()
    ball.reset()
    plat.update()
    plat.reset()
    plat2.update()
    plat2.reset()
    clock.tick(FPS)
    display.update()
