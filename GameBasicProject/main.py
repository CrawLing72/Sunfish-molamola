import sys
import pygame
import globs
import system

#pygame initialization
pygame.init()
pygame.display.set_caption('Frieren : Beyond Journey')

myScreen = pygame.display.set_mode((globs.WINDOW_WIDTH,globs.WINDOW_HEIGHT))
myTextFont = pygame.font.SysFont(globs.COMMON_FONT, 50)
myText = myTextFont.render('Frieren', True, globs.white)
myTextRect = myText.get_rect()
myTextRect.center = (globs.WINDOW_WIDTH/2, globs.WINDOW_HEIGHT/2)

while True:
    myScreen.fill(globs.black)
    myScreen.blit(myText,myTextRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keyEvent = pygame.key.get_pressed()

    if keyEvent[pygame.K_w]:
        print("W Released!")
    elif keyEvent[pygame.K_s]:
        print("S Released!")

    pygame.display.update()
