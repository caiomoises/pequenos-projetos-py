import pygame 
from pygame.locals import *

pygame.init()

altura = 500
largura = 500

x = altura/2
y = largura/2

tela = pygame.display.set_mode((altura, largura))

pygame.display.set_caption('Jogo de Caio')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.guit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                y -= 5
            elif event.key == K_DOWN:
                y += 5
            elif event.key == K_LEFT:
                x -= 5
            elif event.key == K_RIGHT:
                x += 5
    pygame.draw.circle(tela, (255,0,0), (x, y),40)

    #if y > altura:
     #   y = 0
    #y = y+1

    pygame.display.update()