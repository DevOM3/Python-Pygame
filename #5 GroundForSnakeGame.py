from SnakeGameColors import *
import pygame
pygame.init()

screen_width = 480
screen_height = 360

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

    # coloring pygame window
    gameWindow.fill(white)
    pygame.display.update()

pygame.quit()
quit()
