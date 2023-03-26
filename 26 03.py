import pygame as pg
import sys
from grass import Grass
from settings import *
from bar import Bar
import random

pg.init()
screen= pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pg.time.Clock()
grass = Grass("grass.jpg",screen , x, y)
bar_sprites = []
def bars_spawn(bar_sprites,y):
    coord = [110,210,310,410]
    random.shuffle(coord)
    for i in range(3):
        b = Bar(screen, coord[i],y)
        bar_sprites.append(b)

def show_game_over():
    game_over = new Gameover()
    game_over.draw()
    pygame.display.update()
    while True:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
grass1 = Grass('grass.jpg',screen,(SCREEN_WIDTH - 200) // 2,0)
grass2 = Grass('grass.jpg',screen,(SCREEN_WIDTH - 200) // 2, - SCREEN_HEIGHT)
road1 = Road('road.png', screen, (SCREEN_WIDTH-200) // 2,0)
road2 = Road('road.png',screen, (SCREEN_WIDTH-200) // 2,-SCREEN_HEIGHT)
car = Car(screen)
bar_sprites1 = []
bar_sprites2 = []
bars_spawn(bar_sprites1, 0)
bars_spawn(bar_sprites2, -SCREEN_HEIGHT/2)



grass.update()
screen_fill((0,0,0))
pg.display.update()
for i in range(len(bar_sprites)):
    bar_sprites[i].update()
    if bar_sprites[i].rect.y > SCREEN_HEIGHT:
        bar_sprites.pop(i)
        bar_sprites.append(b)



for i in range(len(bar_sprites)):
    bar_sprites[i].draw()    
