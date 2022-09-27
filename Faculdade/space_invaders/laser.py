# criando o laser
    
# uma sprite com uma posição e uma velocidade

import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed,screen_height) :
        super().__init__()
        self.image = pygame.Surface((4,20)) # por que 4 x 20, passei 30 minutos chutando valor esse ficou mais bonito
        self.image.fill('white')
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
        self.height = screen_height
    
    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height + 50:
            self.kill()

    def update(self):
        self.rect.y -= self.speed
        self.destroy()