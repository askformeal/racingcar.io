import sys
import pygame
import json
from time import time

from background import Background
from enemy import Enemy
from player import Player

class Main:
    def __init__(self):
        with open('settings.json') as f:
            self.settings = json.load(f)
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
            print(self.score)

    def check_key_up(self,event):
        if event == pygame.K_a:
            self.player.move_left = False
        elif event == pygame.K_d:
            self.player.move_right = False

    def update_timer(self):
        #self.timer = round(time()-self.start_time,2)
        self.timer+=1

    def draw_score(self):
        self.textsurface = self.font.render(str(self.score), False, (0, 0, 0))
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
            print('game_over')
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
