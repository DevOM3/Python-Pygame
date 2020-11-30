from SnakeGameColors import *
import pygame
pygame.init()

screen_width = 480
screen_height = 360
snake_size = 8
snake_x = 226
snake_y = 176

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

exit_game = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()

pygame.quit()
quit()
