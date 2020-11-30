from SnakeGameColors import *
import pygame

screen_width = 480
screen_height = 360
velocity_x = 0
velocity_y = 0
snake_size = 8
snake_x = 226
snake_y = 176
fps = 50

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
                velocity_x = 0
                velocity_y = -5
            if event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = 5
            if event.key == pygame.K_RIGHT:
                velocity_y = 0
                velocity_x = 5
            if event.key == pygame.K_LEFT:
                velocity_y = 0
                velocity_x = -5

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
