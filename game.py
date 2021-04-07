import random
import pygame
import time


class Game:
    def __init__(self, w, h, cell_size, snake_object, screen):
        self.run = True
        self.score = 0
        self.food_pos = (0, 0)
        self.w = w
        self.h = h
        self.cell_size = cell_size
        self.col = self.w // self.cell_size
        self.row = self.h // self.cell_size
        self.snake = snake_object
        self.snake.list = [(self.col//2, self.row//2)]
        self.screen = screen
        self.drop_food()
        self.speed = 3

    def drop_food(self):
        self.food_pos = (random.randint(1, self.col - 1), random.randint(1, self.row - 1))

    def move_snake(self):
        pass

    def update(self):

        # check eating food
        if self.snake.list[0] == self.food_pos:
            self.score +=1
            self.snake.length += 1
            self.drop_food()
            self.speed += 1

        # check collision
        if self.snake.list[0] in self.snake.list[1:]:
            self.run = False

        # check borders
        if self.snake.list[0][0] == 0 or self.snake.list[0][0] == self.col or self.snake.list[0][1] == 0 or self.snake.list[0][1] == self.row:
            self.run = False

        # black screen
        self.screen.fill((40, 40, 40))

        # draw snake
        for cell in self.snake.list[1:]:
            # print(self.snake.list)
            pygame.draw.rect(self.screen, self.snake.color,
                             [(self.cell_size * cell[0] - self.cell_size / 2 + 1), (self.cell_size * cell[1] - self.cell_size / 2 + 1),
                              self.cell_size - 2, self.cell_size - 2])

        #  draw hat
        pygame.draw.rect(self.screen, (120, 120, 120),
                         [(self.cell_size * self.snake.list[0][0] - self.cell_size / 2 + 1),
                          (self.cell_size * self.snake.list[0][1] - self.cell_size / 2 + 1),
                          self.cell_size - 2, self.cell_size - 2])

        # draw food
        pygame.draw.rect(self.screen, (255, 80, 0),
                             [(self.cell_size * self.food_pos[0] - self.cell_size / 2 + 1), (self.cell_size * self.food_pos[1] - self.cell_size / 2 + 1),
                              self.cell_size - 2, self.cell_size - 2])

        # self.drop_food()

        pygame.display.flip()
        time.sleep(0)