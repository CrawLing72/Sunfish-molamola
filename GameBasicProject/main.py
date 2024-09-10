import sys
import pygame
import globs
import probs
import system

#Note : Now on Contribution!

#pygame initialization
pygame.init()
pygame.display.set_caption('Sunfish : Mola Mola')

myScreen = pygame.display.set_mode((globs.WINDOW_WIDTH,globs.WINDOW_HEIGHT))

clock = pygame.time.Clock()

#Game Loop
def rungame():

    world = system.World(globs.TILE_SIZE, globs.CHUNK_SIZE)
    player_x, player_y = globs.WINDOW_WIDTH/2, globs.WINDOW_HEIGHT/2
    world_offset_x, world_offset_y = 0, 0

    sunfish = probs.Character(globs.ANIPATH,4, player_x, player_y)
    Coordinate_text = probs.Text("X : ???, Y : ???", globs.COMMON_FONT, 20, globs.WHITE)

    delta_time = clock.tick(60) / 1000.0


    while True:
        movement_vector = [0, 0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keyEvent = pygame.key.get_pressed()
        if keyEvent[pygame.K_w]:
            world_offset_y += globs.PLAYER_SPEED * delta_time
            movement_vector[1] = globs.PLAYER_SPEED
        elif keyEvent[pygame.K_s]:
            world_offset_y -= globs.PLAYER_SPEED * delta_time
            movement_vector[1] = -globs.PLAYER_SPEED
        elif keyEvent[pygame.K_a]:
            world_offset_x += globs.PLAYER_SPEED * delta_time
            movement_vector[0] = globs.PLAYER_SPEED
        elif keyEvent[pygame.K_d]:
            world_offset_x -= globs.PLAYER_SPEED * delta_time
            movement_vector[0] = -globs.PLAYER_SPEED

        myScreen.fill(globs.BLACK)

        world.draw(myScreen, player_x, player_y, world_offset_x, world_offset_y)
        sunfish.draw(myScreen, movement_vector[0], movement_vector[1], delta_time)

        Coordinate_text.string = f"X: {-int(world_offset_x/globs.TILE_SIZE)}, Y: {int(world_offset_y/globs.TILE_SIZE)}"
        Coordinate_text.draw(myScreen, 100, 25)

        pygame.display.update()

        clock.tick(globs.FPS)


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


