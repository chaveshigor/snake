import pygame, random
from pygame.locals import * 
from snake import Snake

pygame.init()

###SIZES
size = (width, height) = (500, 500)
screen = pygame.display.set_mode(size)
snakeSize = (15, 15)

###COLORS
black = 10, 10, 10
white = 255, 255, 255
red = 255, 50, 50

snake = Snake()
snakePos = [(200, 200), (210, 200), (220, 200)]
snakeSkin = pygame.Surface(snakeSize)
snakeSkin.fill(white)

applePos = snake.randomGridPosition(size)
appleSkin = pygame.Surface(snakeSize)
appleSkin.fill(red)

clock = pygame.time.Clock()
move = 'up'
running = True

while running:
    clock.tick(30)
    screen.fill(black)

    for event in pygame.event.get():

        if event.type == pygame.QUIT: 
            running = False
    
        elif event.type == KEYDOWN:
            key = event.key

            if event.key == K_LEFT:
                move = 'left'
            if event.key == K_RIGHT:
                move = 'right'
            if event.key == K_DOWN:
                move = 'down'
            if event.key == K_UP:
                move = 'up'

    snakePos = snake.run(snakePos, move, screen, snakeSkin)

    screen.blit(appleSkin, applePos)

    if(snake.colision(snakePos, applePos)):
        applePos = snake.randomGridPosition(size)
        screen.blit(appleSkin, applePos)
        tail = (0, 0)
        snakePos.append(tail)

    pygame.display.update()

