import pygame
import globs
import probs
import noise
import math
import numpy as np

class Chunk:
    def __init__(self, world_x, world_y, tile_size, chunk_size):
        self.world_x = world_x
        self.world_y = world_y # pygame coordinate
        self.tile_size = tile_size
        self.chunk_size = chunk_size
        self.world_seed = globs.WORLD_SEED
        self.tiles = self.generate_tiles()
        self.obj_tiles = self.generate_objs()
        self.tile_imgs = {0: probs.Image(globs.SEA), 1: probs.Image(globs.DEEPSEA), 2: probs.Image(globs.GROUND)}
        self.obj_imgs = {-1: probs.Image(globs.BLANK), 0: probs.Image(globs.TREE), 1: probs.Image(globs.GRASS), 2: probs.Image(globs.MOLAMOLA)}
        self.obj_imgs[2].adjust(45, 45)

    def generate_tiles(self):
        tiles = []
        scale = 100
        for i in range(self.chunk_size):
            row = []
            for j in range(self.chunk_size):
                world_tile_x = self.world_x + j
                world_tile_y = self.world_y + i
                noise_value = noise.pnoise2(world_tile_x / scale, world_tile_y / scale, octaves=6, base=self.world_seed)
                # Perin Noise기반 Connectivity 노리기
                row.append(self.getTileByNoise(noise_value, False))
            tiles.append(row)
        return tiles

    def generate_objs(self):
        tiles = []
        scale = 100
        for i in range(self.chunk_size):
            row = []
            for j in range(self.chunk_size):
                world_tile_x = self.world_x + j
                world_tile_y = self.world_y + i
                noise_value = noise.pnoise2(world_tile_x / scale, world_tile_y / scale, octaves=6, base=self.world_seed)
                # Perin Noise기반 Connectivity 노리기
                row.append(self.getTileByNoise(noise_value, True))
            tiles.append(row)
        return tiles

    def getTileByNoise(self, noise_value, objmode: bool):
        if(objmode):
            if -0.16 < noise_value < -0.15 or -0.13 < noise_value < -0.12:
                img = 1
            elif -0.115 <= noise_value < -0.119 or -0.18 < noise_value < -0.179 :
                img = 0
            elif -0.3 < noise_value < -0.27:
                img = 1
            elif 0 < noise_value < 0.001 or 0.15 < noise_value < 0.1501 or 0.16 < noise_value < 0.161:
                img = 2
            else:
                img = -1
            return img
        else:
            if noise_value < -0.1:
                img = 2 # 육지
            elif noise_value < 0.1:
                img = 1  # 바다
            else:
                img = 0  # 심해  # 디버깅 출력
            return img

    def draw(self, screen, offset_x, offset_y):

        for i, row in enumerate(self.tiles):
            for j, tile in enumerate(row):
                x = self.world_x + j * self.tile_size + offset_x
                y = self.world_y + i * self.tile_size + offset_y #j가 column, i가 row index가 되어야 함에 유의할 것
                temp_tile = self.tile_imgs[tile]
                temp_tile.draw(screen, x, y)

        for i, row in enumerate(self.obj_tiles):
            for j, tile in enumerate(row):
                if tile >= 0:
                    x = self.world_x + j * self.tile_size + offset_x
                    y = self.world_y + i * self.tile_size + offset_y
                    temp_tile = self.obj_imgs[tile]
                    temp_tile.draw(screen, x, y)


class World:
    def __init__(self, tile_size, chunk_size):
        self.tile_size = tile_size
        self.chunk_size = chunk_size
        self.chunks = {}
        self.previous_chunk_x = None
        self.previous_chunk_y = None

    def get_chunk(self, chunk_x, chunk_y):
        if (chunk_x, chunk_y) not in self.chunks:
            # 새로운 청크를 생성할 때만 로그 출력
            print(f"Generating new chunk at ({chunk_x}, {chunk_y})")
            self.chunks[(chunk_x, chunk_y)] = Chunk(chunk_x * self.chunk_size * self.tile_size,
                                                    chunk_y * self.chunk_size * self.tile_size, self.tile_size,
                                                    self.chunk_size)
        return self.chunks[(chunk_x, chunk_y)]

    def draw(self, screen, player_x, player_y, offset_x, offset_y):
        ## WARNING :: Chunk Coordinate is USING PYGAME COORDINATE
        current_chunk_x = int(globs.WINDOW_WIDTH/2 -offset_x) // (self.chunk_size * self.tile_size)
        current_chunk_y = int(globs.WINDOW_HEIGHT/2 -offset_y) // (self.chunk_size * self.tile_size)

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                chunk = self.get_chunk(current_chunk_x + dx, current_chunk_y + dy)
                chunk.draw(screen, offset_x, offset_y)

    def get_tile_info(self, offset_x, offset_y, is_tiles: bool = True, is_load: bool = False, write_value: int = 0):
        # 화면 중앙 좌표 (플레이어가 항상 고정된 위치)
        screen_center_x = globs.WINDOW_WIDTH // 2
        screen_center_y = globs.WINDOW_HEIGHT // 2

        # 플레이어의 월드 좌표 (화면 중앙 기준으로 오프셋 적용)
        world_center_x = screen_center_x - offset_x
        world_center_y = screen_center_y - offset_y

        # 타일 크기의 절반 값을 보정하여 타일 중심을 기준으로 계산
        world_center_x += self.tile_size // 2
        world_center_y += self.tile_size // 2

        # 청크 좌표 계산
        current_chunk_x = math.floor(world_center_x / (self.chunk_size * self.tile_size))
        current_chunk_y = math.floor(world_center_y / (self.chunk_size * self.tile_size))

        # 현재 청크 가져오기
        if (current_chunk_x, current_chunk_y) not in self.chunks:
            print(f"Chunk ({current_chunk_x}, {current_chunk_y}) not found!")
            return None

        current_chunk = self.chunks[(current_chunk_x, current_chunk_y)]
        chunk_tiles = current_chunk.tiles

        # 청크 내에서 타일 좌표 계산 (타일의 중심을 기준으로 계산)
        tile_x_in_chunk = int((world_center_x - current_chunk.world_x + 20) // self.tile_size)
        tile_y_in_chunk = int((world_center_y - current_chunk.world_y + 20) // self.tile_size)

        # 경계 처리를 위해 타일 인덱스가 청크 범위를 벗어나는지 확인
        if tile_x_in_chunk >= self.chunk_size:
            current_chunk_x += 1
            tile_x_in_chunk = 0
        elif tile_x_in_chunk < 0:
            current_chunk_x -= 1
            tile_x_in_chunk = self.chunk_size - 1

        if tile_y_in_chunk >= self.chunk_size:
            current_chunk_y += 1
            tile_y_in_chunk = 0
        elif tile_y_in_chunk < 0:
            current_chunk_y -= 1
            tile_y_in_chunk = self.chunk_size - 1

        final_result = 0

        # 경계를 넘어서면 새로운 청크에서 타일을 가져오기
        if (current_chunk_x, current_chunk_y) in self.chunks:
            current_chunk = self.chunks[(current_chunk_x, current_chunk_y)]
            chunk_tiles = current_chunk.tiles

            # 타일 정보 출력
        if not is_load:
            if 0 <= tile_x_in_chunk < self.chunk_size and 0 <= tile_y_in_chunk < self.chunk_size:
                if (is_tiles):
                    final_result = chunk_tiles[tile_y_in_chunk][tile_x_in_chunk]
                else:
                    final_result = current_chunk.obj_tiles[tile_y_in_chunk][tile_x_in_chunk]

            else:
                print("Invalid tile index!")

            return final_result
        else:
            if 0 <= tile_x_in_chunk < self.chunk_size and 0 <= tile_y_in_chunk < self.chunk_size:
                if (is_tiles):
                    chunk_tiles[tile_y_in_chunk][tile_x_in_chunk] = write_value
                else:
                    current_chunk.obj_tiles[tile_y_in_chunk][tile_x_in_chunk] = write_value