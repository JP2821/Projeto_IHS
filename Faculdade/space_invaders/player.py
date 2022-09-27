# definições de um player

# 1. mostrar a imagem do próprio jogador
# 2. deve ser capaz de se mover
# 3. o movimeto deve ser restrito ao tamanho da tela
# 4. capaz de disparar o laser e recarregar

import pygame

from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,size_width,speed):
        super().__init__()
        self.image = pygame.image.load('C:/Users/jotap/vscode/Faculdade/graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.witdh = size_width
        self.speed = speed
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600 # tempo em milisegundos
        self.lasers = pygame.sprite.Group()
    
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            largura,altura = self.rect.size
            if self.rect.x >= (self.witdh - largura):
                self.rect.x = self.witdh - largura

        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.rect.x = 0 
        
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center,self.speed,self.rect.bottom))

    def update(self):
        self.get_input()
        self.recharge()
        self.lasers.update()
        