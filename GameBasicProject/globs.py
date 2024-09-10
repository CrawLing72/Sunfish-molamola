import random
import probs
import time

#Screen Parameter
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 702

#Font Parameter
COMMON_FONT = "./Resources/NanumMyeongjoBold.ttf"

#Color Parameter
BLACK = (0,0,0)
WHITE = (255,255,255)

## chunk and tiles
TILE_SIZE = 48
CHUNK_SIZE = 24

## Player Movement Related
PLAYER_SPEED = 5

## Env Related
WORLD_SEED = random.randint(0, 300)
FPS = 60

# Tile Path
SEA = "./Resources/imgs/images/normalsea.png"
GROUND = "./Resources/imgs/images/ground.png"
DEEPSEA = "./Resources/imgs/images/deepsea.png"



# ANIMATION PATH
w_path = [probs.Image(f"./Resources/imgs/images/Elaina_Rung_Back_0{i}.png") for i in range(1, 7)]
s_path = [probs.Image(f"./Resources/imgs/images/Elaina_Run_Fr_0{i}.png") for i in range(1, 7)]
d_path = [probs.Image(f"./Resources/imgs/images/Elaina_Run_lf_0{i}.png") for i in range(1, 7)]
a_path = [probs.Image(f"./Resources/imgs/images/Elaina_Run_Rt_0{i}.png") for i in range(1, 7)]
waiting_path = [probs.Image(f"./Resources/imgs/images/Elaina_Front_0{i}.png") for i in range(1, 5)]
ANIPATH = {"w" : w_path, "s" : s_path, "a" : a_path, "d" : d_path, "e" : waiting_path}
