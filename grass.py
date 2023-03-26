import pygame as pg

class Grass(pg.sprite.Sprite):
    def __init__(self,filename,screen, x, y):
        self.screen = screen
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
    def update(self):
        self.rect.y +=2
        if self.rect>= 1000:
            self.rect.y = -1000
    def draw(self):
        self.screen.blit(self.image,self.rect)
