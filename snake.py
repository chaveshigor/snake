import pygame, random
from pygame.locals import *

white = 255, 255, 255
black = 10, 10, 10
red = 255, 0, 10

clock=pygame.time.Clock()
FPS=30

class Snake:

    def __init__(self):
        pass

    def run(self, snake, move, screen, snakeSkin):
        if move == 'left':
            snake[0] = (snake[0][0] - 5, snake[0][1]) 

        elif move == 'right':
            snake[0] = (snake[0][0] + 5, snake[0][1])

        elif move == 'down':
            snake[0] = (snake[0][0], snake[0][1] + 5)

        elif move == 'up':
            snake[0] = (snake[0][0], snake[0][1] - 5)

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])
    
        for pos in snake:
            screen.blit(snakeSkin,pos)

        return snake

    
    def randomGridPosition(self, size):

        width = random.randint(0, size[0])
        height = random.randint(0, size[1])

        width = width - width%20
        height = height - height%20

        return (width, height)

    def colision(self, snake, block):

        snakeHead = snake[0]

        if snakeHead == block:
            return True

        else:
            return False


                
