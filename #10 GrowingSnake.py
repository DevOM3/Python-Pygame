from SnakeGameColors import *
import random
import pygame
pygame.init()

screen_width = 650
screen_height = 450
food_x = random.randint(20, screen_width - 20)
food_y = random.randint(20, screen_height - 20)
food_radius = 5
velocity_x = 0
velocity_y = 0
snake_size = 10
snake_y = 175
snake_x = 235
score = 0
fps = 50

snake_length = 1
snake_list = []

clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 21)

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")


def show_on_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def grow_snake(base, color, ordinates, size):
    for x, y in ordinates:
        pygame.draw.rect(base, color, [x, y, size, size])


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
        snake_length = snake_length + 3
        food_x = random.randint(20, screen_width - 20)
        food_y = random.randint(20, screen_height - 20)
    elif abs(food_x - snake_x) < 5 and abs(food_y - snake_y) < 5:
        score = score + 10
        snake_length = snake_length + 3
        food_x = random.randint(20, screen_width - 20)
        food_y = random.randint(20, screen_height - 20)

    gameWindow.fill(white)

    show_on_screen("Score : " + str(score), purple, 10, 10)

    pygame.draw.circle(gameWindow, red, [food_x, food_y], food_radius)

    snake_head = list()
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    grow_snake(gameWindow, black, snake_list, snake_size)
    pygame.display.update()

    clock.tick(fps)

pygame.quit()
quit()
