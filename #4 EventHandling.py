import pygame
pygame.init()

gameWindow = pygame.display.set_mode((251, 451))
pygame.display.set_caption("Event Handling")

exit_game = False
while not exit_game:
    for event in pygame.event.get():
        # closing a game window
        if event.type == pygame.QUIT:
            exit_game = True

        elif event.type == pygame.KEYDOWN:
            print(chr(event.key))

pygame.quit()
quit()
