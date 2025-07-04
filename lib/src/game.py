import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# background image
BACKGROUND = pygame.image.load('lib/assets/other/red_background.jpg')
BACKGROUND = BACKGROUND.convert() # faster rendering

run = True

# game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # add the background image
    SCREEN.blit(BACKGROUND, (0, 0))
    pygame.display.flip()
    

pygame.quit() 