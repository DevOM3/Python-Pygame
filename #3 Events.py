import pygame
pygame.init()

gameWindow = pygame.display.set_mode((251, 451))
pygame.display.set_caption("Pygame Events")

exit_game = False
while not exit_game:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()
