import pygame
from pygame.locals import *
from random import randint

def get_maca_pos():
    x = randint(10, 580)
    y = randint(10, 580)
    return (x//10 * 10, y//10 * 10)

def colisao(c, m):
    if c[0] == m[0] and c[1] == m[1]:
        return True
    else:
        return False

CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

pygame.init()
tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))
snake_direcao = ESQUERDA

maca_pos = get_maca_pos()
maca_skin = pygame.Surface((10, 10))
maca_skin.fill((255, 0, 0))

clock = pygame.time.Clock()
while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                snake_direcao = CIMA

            elif event.key == K_RIGHT:
                snake_direcao = DIREITA

            elif event.key == K_DOWN:
                snake_direcao = BAIXO

            elif event.key == K_LEFT:
                snake_direcao = ESQUERDA

    if colisao(snake[0], maca_pos):
        snake.append(maca_pos)
        maca_pos = get_maca_pos()

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if snake_direcao == CIMA:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    elif snake_direcao == DIREITA:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    elif snake_direcao == BAIXO:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    elif snake_direcao == ESQUERDA:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    tela.fill((0, 0, 0))
    tela.blit(maca_skin, maca_pos)
    for pos in snake:
        tela.blit(snake_skin, pos)

    pygame.display.update()

