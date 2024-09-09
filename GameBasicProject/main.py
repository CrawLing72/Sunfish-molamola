import sys
import pygame
import globs
import probs
import system

#pygame initialization
pygame.init()
pygame.display.set_caption('Sunfish : Mola Mola')

myScreen = pygame.display.set_mode((globs.WINDOW_WIDTH,globs.WINDOW_HEIGHT), pygame.FULLSCREEN)

#Game Loop
def rungame():
    while True:
        myScreen.fill(globs.BLACK)

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


def main_menu():
    button = probs.Button("./Resources/imgs/Sunfish_White.png", rungame)
    mainimage = probs.Image("./Resources/imgs/MainArt.png")
    intro_text = probs.Text("Click the logo to start", globs.COMMON_FONT, 30, globs.BLACK)

    while True:
        myScreen.fill(globs.BLACK)

        mainimage.draw(myScreen, globs.WINDOW_WIDTH/2, globs.WINDOW_HEIGHT/2)
        button.draw(globs.WINDOW_WIDTH/2, globs.WINDOW_HEIGHT/2, myScreen)
        intro_text.draw(myScreen, globs.WINDOW_WIDTH/2, globs.WINDOW_HEIGHT/2 + 130)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button.detection()

        pygame.display.update()

main_menu()


