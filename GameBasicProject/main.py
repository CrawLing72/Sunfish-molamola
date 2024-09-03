import sys

import pygame

#pygame initialization
pygame.init()
pygame.display.set_caption('Frieren : Beyond Journey')

myscreen = pygame.display.set_mode((1600,900))
myTextFont = pygame.font.SysFont('Arial', 50)
myText = myTextFont.render('Frieren', True, (255,255,255))
myTextRect = myText.get_rect()
myTextRect.center = (800, 450)

while True:
    myscreen.fill((0,0,0))
    myscreen.blit(myText,myTextRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
