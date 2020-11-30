from SnakeGameColors import *
import random
import pygame
import os
pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

screen_width = 650
screen_height = 450

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

start_bg = pygame.image.load("start.jpg")
start_bg = pygame.transform.scale(start_bg, (screen_width, screen_height)).convert_alpha()

game_bg = pygame.image.load("grass.png")
game_bg = pygame.transform.scale(game_bg, (screen_width, screen_width)).convert_alpha()

over_bg = pygame.image.load("over.jpg")
over_bg = pygame.transform.scale(over_bg, (screen_width, screen_height)).convert_alpha()


def start():
    exit_game = False
    pygame.mixer.music.load("intro.mp3")
    pygame.mixer.music.play(-1)
    while not exit_game:
        gameWindow.fill(yellow)
        gameWindow.blit(start_bg, (0, 0))
        show_on_screen("Press Any Key to Start the Game......", black, 160, 57)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                game_loop()
        pygame.display.update()
        clock.tick(60)


def show_on_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def grow_snake(base, color, ordinates, size):
    for x, y in ordinates:
        pygame.draw.rect(base, color, [x, y, size, size])


def game_loop():
    if not os.path.exists("high_score.txt"):
        with open("high_score.txt", "w") as hs:
            hs.write("0")
    with open("high_score.txt", "r") as hs:
        high_score = hs.read()

    pygame.mixer.music.load("bg.mp3")
    pygame.mixer.music.play(-1)

    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(75, screen_height - 20)
    food_radius = 5
    velocity_x = 0
    velocity_y = 0
    snake_size = 10
    snake_y = 220
    snake_x = 320
    score = 0
    fps = 50

    snake_length = 1
    snake_list = []

    exit_game = False
    game_over = False

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            gameWindow.blit(game_bg, (0, 0))
            show_on_screen("Game Over!!! Press Return to Continue", red, 130, 160)
            show_on_screen("Your Score : " + str(score), red, 230, 180)
            show_on_screen("High Score : " + str(high_score), red, 230, 200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_over = False
                        game_loop()

        else:
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
                # pygame.mixer.music.load("food.mp3")
                # pygame.mixer.music.play()
                score = score + 10
                snake_length = snake_length + 3
                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(50, screen_height - 20)
                # pygame.mixer.music.load("bg.mp3")
                # pygame.mixer.music.play(-1)
            elif abs(food_x - snake_x) < 5 and abs(food_y - snake_y) < 5:
                # pygame.mixer.music.load("food.mp3")
                # pygame.mixer.music.play()
                score = score + 10
                snake_length = snake_length + 3
                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(50, screen_height - 20)
                # pygame.mixer.music.load("bg.mp3")
                # pygame.mixer.music.play(-1)

            gameWindow.fill(white)
            gameWindow.blit(game_bg, (0, 0))
            show_on_screen("Score : " + str(score) + "                 High Score : " + str(high_score), purple, 10, 10)
            pygame.draw.line(gameWindow, brown, (0, 40), (screen_width, 40), 3)
            pygame.draw.circle(gameWindow, red, [food_x, food_y], food_radius)

            snake_head = list()
            snake_head.append(snake_x)
            snake_head.append(snake_y)
            snake_list.append(snake_head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if snake_head in snake_list[:-1]:
                pygame.mixer.music.load("over.mp3")
                pygame.mixer.music.play()
                if int(high_score) <= score:
                    with open("high_score.txt", "w") as hs:
                        hs.write(str(score))
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 40 or snake_y > screen_height:
                pygame.mixer.music.load("over.mp3")
                pygame.mixer.music.play()
                if int(high_score) <= score:
                    with open("high_score.txt", "w") as hs:
                        hs.write(str(score))
                game_over = True

            if int(high_score) < score:
                high_score = score

            grow_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


start()
