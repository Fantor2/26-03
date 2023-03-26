from settings import *
import pygame

class Bar(pygame.sprite.Sprite):

    def __init__(self,screen,x,y):
        self.screen=screen
        pygame.sprite.Sprite.__init(self)
        self.image = pygame.image.load(BAR_FILE_NAME).convert_alpha()
        self.rect = self.imgae.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = 2

    def update(self):
        self.rect.y +=self.speedy
    def draw(self):
        self.screen_blit(self.image,self.rect)
