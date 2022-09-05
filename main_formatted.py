from random import randint
import sys
import pygame
from pygame.sprite import Sprite
import json
from time import time

class Player:
    def __init__(self,main):
        self.main = main
        self.screen = main.screen
        self.image = pygame.image.load('car1.png')
        self.rect = self.image.get_rect()
        self.y = 450
        self.rect.y = self.y
        self.x = 245

        self.move_left = False
        self.move_right = False

    def update(self):
        self.rect.x = self.x
        self.screen.blit(self.image,(self.x,self.y))
        if self.move_left:
            self.x -= 1
        elif self.move_right:
            self.x += 1

        if self.x < 68 or self.x > 440:
            #self.main.running = False
            if self.move_left:
                self.x += 1
            elif self.move_right:
                self.x -= 1

class Enemy(Sprite):
    def __init__(self,main):
        super().__init__()
        self.main = main
        self.screen = main.screen
        self.image = pygame.image.load('car2.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(68,440)
        self.y = -100
    
    def update(self):
        if self.main.timer > 1200:
            self.screen.blit(self.image,(self.rect.x,self.y))
            self.y += 1.3
            self.rect.y = self.y

class Background:
    def __init__(self,main):
        self.screen = main.screen
        self.main = main
        self.image = pygame.image.load('back.bmp')
        self.y = -586
        
    def update(self):
        self.screen.blit(self.image,(0,self.y))
        self.y += 1
        if self.y >= 0:
            self.y = -586

class Main:
    def __init__(self):
        self.settings = {"screen_width":558,"screen_height":586,"bg_color":[255,255,255]}
        self.screen = pygame.display.set_mode((self.settings['screen_width'],
        self.settings['screen_height']))

        pygame.display.set_caption('Racing Car!')
        pygame.display.set_icon(pygame.image.load('icon.png'))

        self.running = True
        #print(self.settings)
        self.background = Background(self)
        self.player = Player(self)
        self.enemies = pygame.sprite.Group()
        self.start_time = time()
        self.timer = 0
        self.score = 0
        pygame.font.init()
        self.font = pygame.font.SysFont('Consolas', 30)
        self.textsurface = None
        pygame.mixer.init()
        pygame.mixer.music.load('Hurry_Up.mp3')
        pygame.mixer.music.play(loops=-1)
        
    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_key_down(event.key)
            elif event.type == pygame.KEYUP:
                self.check_key_up(event.key)

    
    def check_key_down(self,event):
        if event == pygame.K_a:
            self.player.move_left = True
        elif event == pygame.K_d:
            self.player.move_right = True
        elif event == pygame.K_t:
            print('''Game made by Li Muzhi, @askformeal on Github. Images and sound effects from @sipspatidar's repository "car_racing". Get permission before use.''')

    def check_key_up(self,event):
        if event == pygame.K_a:
            self.player.move_left = False
        elif event == pygame.K_d:
            self.player.move_right = False

    def update_timer(self):
        #self.timer = round(time()-self.start_time,2)
        self.timer+=1

    def draw_score(self):
        self.textsurface = self.font.render(str(self.score), False, (255, 255, 255))
        self.screen.blit(self.textsurface,(0,0))
        
    def update_enemy(self):
        self.enemies.update()
        if self.timer%700 == 0 and self.timer > 1200:
            self.enemies.add(Enemy(self))
        for enemy in self.enemies:
            if enemy.rect.y >= self.settings['screen_height']:
                enemy.kill()
                self.score += 1
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.running = False

    def update(self):
        #bg_color = tuple(self.settings['bg_color'])
        #self.screen.fill(bg_color)

        self.background.update()
        self.player.update()
        self.update_enemy()

        self.update_timer()
        self.draw_score()

        pygame.display.flip()

    def run(self):
        while self.running:
            self.update()
            self.check()
        pygame.mixer.music.stop()
        gameover = pygame.image.load('game_over.bmp')
        self.screen.blit(gameover,(0,0))
        while True:
            self.textsurface = self.font.render(f'Your score:{str(self.score)}', False, (0, 0, 0))
            self.screen.blit(self.textsurface,(125,312))
            pygame.display.flip()
            self.check()



if __name__ == '__main__':
    main = Main()
    main.run()
