import sys
import pygame
import globs
import probs
import system

#Note : Now on Contribution!

#pygame initialization
pygame.init()
pygame.display.set_caption('Sunfish : Mola Mola')
pygame.display.set_icon(pygame.image.load("./Resources/imgs/images/ocean_sunfish_128.png"))

myScreen = pygame.display.set_mode((globs.WINDOW_WIDTH,globs.WINDOW_HEIGHT))

clock = pygame.time.Clock()

#Game Loop
def rungame():

    #World Setting
    world = system.World(globs.TILE_SIZE, globs.CHUNK_SIZE)
    player_x, player_y = globs.WINDOW_WIDTH/2, globs.WINDOW_HEIGHT/2
    world_offset_x, world_offset_y = 0, 0

    #asset setting
    Elaina = probs.Character(globs.ANIPATH,8, player_x, player_y)
    Coordinate_text = probs.Text("X : ???, Y : ???", globs.COMMON_FONT, 20, globs.WHITE)
    Tile_text = probs.Text("You are on the ####", globs.COMMON_FONT, 10, globs.WHITE)
    Count_text = probs.Text("You got # molamola!", globs.COMMON_FONT, 20, globs.WHITE)
    Ballons = probs.Image("./Resources/imgs/images/ballon_90px.png")
    Arrows = probs.Image(globs.ARROW)
    # WARNING : Coordinate text is just displaying. Please CONSIDER PYGAME SYSTEM!

    #Time Settings
    delta_time = clock.tick(60) / 1000.0

    #Bool & Conditions
    is_ballon_on = False
    count_of_molamoala = 0

    #Game Loop
    while True:
        movement_vector = [0, 0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #Key Event Sector
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

        #tile info handling
        tile_info = world.get_tile_info(world_offset_x, world_offset_y)
        if tile_info == 0:
            globs.PLAYER_SPEED = 7
            is_ballon_on = True
        elif tile_info == 1:
            globs.PLAYER_SPEED = 5
            is_ballon_on = True
        elif tile_info == 2:
            globs.PLAYER_SPEED = 10
            is_ballon_on = False
        else:
            tile_info = 0

        #Object info Handling
        object_info = world.get_tile_info(world_offset_x, world_offset_y, False)
        if object_info == 2 and keyEvent[pygame.K_SPACE]:
            world.get_tile_info(world_offset_x, world_offset_y, False, True, -1)
            count_of_molamoala += 1

        myScreen.fill(globs.BLACK)

        # Drawing Sector
        world.draw(myScreen, player_x, player_y, world_offset_x, world_offset_y)
        if (is_ballon_on):
            Ballons.draw(myScreen, globs.WINDOW_WIDTH/2 + 20, globs.WINDOW_HEIGHT/2 - 40)
        Elaina.draw(myScreen, movement_vector[0], movement_vector[1], delta_time)
        Arrows.draw(myScreen, player_x, player_y)

        #Text Drawing Sector
        Coordinate_text.string = f"X: {-int(world_offset_x/globs.TILE_SIZE)}, Y: {int(world_offset_y/globs.TILE_SIZE)}"
        Coordinate_text.draw(myScreen, 100, 25)
        Tile_text.string = f"You're on the {globs.TILEINFO[tile_info]}!"
        Tile_text.draw(myScreen, 80, 45)
        Count_text.string = f"You got {count_of_molamoala} molamola!"
        Count_text.draw(myScreen, globs.WINDOW_WIDTH - 120, 25)

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


