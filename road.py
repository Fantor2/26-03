import pygame as pg
import from settings *

class Road(pg.sprite.Sprite):
    def __init__(self,filename,screen, x, y):
        self.screen=screen
        pygame.sprite.Sprite.__init(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.imgae.get_rect()
        self.rect.center.x = x
        self.rect.top.y = y
    def update(self):
        self.rect.y += 2
        if self.rect.y >= 1000:
            self.rect.y = -1000
    def draw(self):
        self.screen_blit(self.image,self.rect)
