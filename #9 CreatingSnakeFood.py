from SnakeGameColors import *
import random
import pygame
pygame.init()

screen_width = 650
screen_height = 450
food_x = random.randint(20, screen_width - 20)
food_y = random.randint(20, screen_height - 20)
food_radius = 4
velocity_x = 0
velocity_y = 0
snake_size = 10
snake_y = 175
snake_x = 235
score = 0
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
                velocity_y = -5
                velocity_x = 0
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

    if abs(snake_x - food_x) < 5 and abs(snake_y - food_y) < 5:
        score = score + 10
        food_x = random.randint(20, screen_width - 20)
        food_y = random.randint(20, screen_height - 20)

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.draw.circle(gameWindow, red, [food_x, food_y], food_radius)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
