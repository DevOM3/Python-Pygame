from SnakeGameColors import *
import pygame
pygame.init()

screen_width = 480
screen_height = 360
snake_size = 8
snake_x = 226
snake_y = 176
fps = 60

clock = pygame.time.Clock()

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

exit_game = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_y = snake_y - 1
            if event.key == pygame.K_DOWN:
                snake_y = snake_y + 1
            if event.key == pygame.K_LEFT:
                snake_x = snake_x - 1
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 1

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    clock.tick(fps)
    pygame.display.update()

pygame.quit()
quit()
