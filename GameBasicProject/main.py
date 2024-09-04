import sys
import pygame
import globs
import probs
import system

#pygame initialization
pygame.init()
pygame.display.set_caption('Frieren : Beyond Journey')

myScreen = pygame.display.set_mode((globs.WINDOW_WIDTH,globs.WINDOW_HEIGHT))

helloWolrd = probs.Text("Hello, world!", globs.COMMON_FONT)
elainaImage = probs.Image("./Resources/Animation/Elaina_Sliced/images/Elaina_Right_01.png")
elainaButton = probs.Button("./Resources/Animation/Elaina_Sliced/images/Elaina_Right_01.png", print("Hello, Button"))

#Game Loop
while True:
    myScreen.fill(globs.black)
    elainaButton.draw(globs.WINDOW_WIDTH/2, globs.WINDOW_HEIGHT/2, 45, 45, myScreen)
    elainaButton.detection()

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
