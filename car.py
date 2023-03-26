import pygame as pg
import random from randint


class Car(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("car.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speedx = 10

        if keys[pg.K_LEFT]
        x -= 5
        if keys[pg.K_RIGHT]
        x += 5
