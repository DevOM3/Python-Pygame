from MultiplayerColor import *
import random
import pygame
pygame.init()

screen_width = 400
screen_height = 600
fps = 30

font = pygame.font.SysFont(None, 55)


def show_text(text, color, x, y):
    text_to_be_shown = font.render(text, True, color)
    gameWindow.blit(text_to_be_shown, [x, y])


def make_rect(window, color, x, y, width, height):
    pygame.draw.rect(window, color, [x, y, width, height])


gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fighter Duos")
clock = pygame.time.Clock()


def start():
    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                game_loop()
        show_text("Press Any Key", random.choice([white, yellow]), 60, 200)
        show_text("to", yellow, 180, 250)
        show_text("S T A R T", random.choice([white, red, green, brown]), 115, 300)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


def over(left_score, right_score):
    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
        gameWindow.fill(black)
        show_text(str(left_score) + " : " + str(right_score), yellow, 160, 200)
        show_text("Press Return", random.choice([white, red, green, brown]), 85, 250)
        show_text("to", yellow, 180, 300)
        show_text("R E S T A R T", random.choice([white, red, green, brown]), 80, 350)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


def game_loop():
    pygame.mixer.music.load("mpbgm.mp3")
    pygame.mixer.music.play(-1)

    bg = pygame.image.load("mpbg.jpg")
    bg = pygame.transform.scale(bg, (screen_width, screen_height)).convert_alpha()

    p = 0
    exit_game = False
    collapse = None

    object_width = 10
    object_height = 75

    object_a_x = screen_width - 12
    object_a_y = 250
    object_b_x = 2
    object_b_y = 250

    ball_velocity_x = 0
    ball_velocity_y = 0
    ball_radius = 5
    ball_x = screen_width // 2
    ball_y = 285

    left_score = 0
    right_score = 0

    old_velocity_x = random.randrange(2, 4)
    old_velocity_y = random.randrange(2, 4)

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if p == 0:
                        ball_velocity_x = old_velocity_x
                        ball_velocity_y = old_velocity_y
                        p = 1
                    elif p == 1:
                        old_velocity_x = ball_velocity_x
                        old_velocity_y = ball_velocity_y
                        ball_velocity_x = 0
                        ball_velocity_y = 0
                        p = 0

        key_hold = pygame.key.get_pressed()
        if key_hold[pygame.K_UP]:
            if not object_a_y <= 60:
                object_a_y = object_a_y - 10
        if key_hold[pygame.K_DOWN]:
            if not object_a_y >= screen_height - 80:
                object_a_y = object_a_y + 10
        if key_hold[pygame.K_w]:
            if not object_b_y <= 60:
                object_b_y = object_b_y - 10
        if key_hold[pygame.K_s]:
            if not object_b_y >= screen_height - 80:
                object_b_y = object_b_y + 10

        if ball_x < 0:
            right_score = right_score + 1
            ball_x = screen_width // 2
            ball_y = 285
            ball_velocity_y = 0
            ball_velocity_x = 0
            p = 0
            old_velocity_y = random.randrange(0, 4)
            if right_score == 3:
                over(left_score, right_score)
        if ball_x > screen_width:
            left_score = left_score + 1
            ball_x = screen_width // 2
            ball_y = 285
            ball_velocity_y = 0
            ball_velocity_x = 0
            p = 0
            old_velocity_y = random.choice([random.randrange(-4, -2), random.randrange(2, 4)])
            old_velocity_x = random.choice([random.randrange(-4, -2), random.randrange(2, 4)])
            if left_score == 3:
                over(left_score, right_score)

        if abs(object_a_x - ball_x) < 3 and (object_a_y < ball_y) and (ball_y < (object_a_y + 75)):
            collapse = "right"
            var = random.randrange(0, 13)
            if var == 1:
                ball_velocity_x = -1
                ball_velocity_y = -4
            if var == 2:
                ball_velocity_x = -2
                ball_velocity_y = -4
            if var == 3:
                ball_velocity_x = -3
                ball_velocity_y = -4
            if var == 4:
                ball_velocity_x = -4
                ball_velocity_y = -4
            if var == 5:
                ball_velocity_x = -4
                ball_velocity_y = -3
            if var == 6:
                ball_velocity_x = -4
                ball_velocity_y = -2
            if var == 7:
                ball_velocity_x = -4
                ball_velocity_y = -1
            if var == 8:
                ball_velocity_x = -4
                ball_velocity_y = 1
            if var == 9:
                ball_velocity_x = -4
                ball_velocity_y = 2
            if var == 10:
                ball_velocity_x = -4
                ball_velocity_y = 3
            if var == 11:
                ball_velocity_x = -4
                ball_velocity_y = 4
            if var == 12:
                ball_velocity_x = -4
                ball_velocity_y = 4
        if abs((object_b_x + 10) - ball_x) < 3 and (object_b_y < ball_y) and (ball_y < (object_b_y + 75)):
            collapse = "left"
            var = random.randrange(0, 12)
            if var == 1:
                ball_velocity_x = 1
                ball_velocity_y = -4
            if var == 2:
                ball_velocity_x = 2
                ball_velocity_y = -4
            if var == 3:
                ball_velocity_x = 3
                ball_velocity_y = -4
            if var == 4:
                ball_velocity_x = 4
                ball_velocity_y = -4
            if var == 5:
                ball_velocity_x = 4
                ball_velocity_y = -3
            if var == 6:
                ball_velocity_x = 4
                ball_velocity_y = -2
            if var == 7:
                ball_velocity_x = 4
                ball_velocity_y = -1
            if var == 8:
                ball_velocity_x = 4
                ball_velocity_y = 1
            if var == 9:
                ball_velocity_x = 4
                ball_velocity_y = 2
            if var == 10:
                ball_velocity_x = 4
                ball_velocity_y = 3
            if var == 11:
                ball_velocity_x = 4
                ball_velocity_y = 4

        if ball_y < 52:
            if collapse == "right":
                ball_velocity_x = -4
                ball_velocity_y = 2
            if collapse == "left":
                ball_velocity_x = 4
                ball_velocity_y = 2
        if ball_y > screen_height - 3:
            if collapse == "right":
                ball_velocity_x = -4
                ball_velocity_y = -2
            if collapse == "left":
                ball_velocity_x = 4
                ball_velocity_y = -2

        ball_x = ball_x + ball_velocity_x
        ball_y = ball_y + ball_velocity_y

        gameWindow.fill(white)
        gameWindow.blit(bg, (0, 0))
        show_text("         " + str(left_score), brown, 2, 7)
        show_text(str(right_score), brown, screen_width - 100, 7)
        pygame.draw.line(gameWindow, black, (0, 50), (screen_width, 50), 3)
        pygame.draw.line(gameWindow, black, (screen_width // 2, 0), (screen_width // 2, 50), 3)
        pygame.draw.line(gameWindow, black, (0, screen_height - 2), (screen_width, screen_height - 2), 3)
        make_rect(gameWindow, black, object_a_x, object_a_y, object_width, object_height)
        make_rect(gameWindow, black, object_b_x, object_b_y, object_width, object_height)
        pygame.draw.circle(gameWindow, red, (ball_x, ball_y), ball_radius)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


pygame.mixer.music.load("mpstart.mp3")
pygame.mixer.music.play(-1)
start()
