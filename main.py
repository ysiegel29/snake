from game import Game
from snake import Snake
import pygame
from pygame.locals import *
import sys

pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

fps = 3
fpsClock = pygame.time.Clock()

WIDTH, HEIGHT = 720, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#  create snake and game instances
_snake = Snake((90, 90, 90))
game = Game(WIDTH, HEIGHT, 20, _snake, screen)


while game.run:
    moved = False
    for event in pygame.event.get():
        # print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                print('UP')
                _snake.move('UP')
            if event.key == K_DOWN:
                print('DOWN')
                _snake.move('DOWN')
            if event.key == K_LEFT:
                print('LEFT')
                _snake.move('LEFT')
            if event.key == K_RIGHT:
                print('RIGHT')
                _snake.move('RIGHT')
            moved = True

    if not moved:
        _snake.move(_snake.direction)

    game.update()
    fps = game.speed
    fpsClock.tick(fps)

pygame.quit()
sys.exit()

