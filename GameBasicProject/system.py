import pygame
import globs
import probs
import noise
import numpy as np

class Chunk:
    def __init__(self, world_x, world_y, tile_size, chunk_size):
        self.world_x = world_x
        self.world_y = world_y
        self.tile_size = tile_size
        self.chunk_size = chunk_size
        self.world_seed = globs.WORLD_SEED
        self.tiles = self.generate_tiles()

    def generate_tiles(self):
        tiles = []
        scale = 100
        for i in range(self.chunk_size):
            row = []
            for j in range(self.chunk_size):
                world_tile_x = self.world_x + i
                world_tile_y = self.world_y + j
                noise_value = noise.pnoise2(world_tile_x / scale, world_tile_y / scale, octaves=6, base=self.world_seed)
                # Perin Noise기반 Connectivity 노리기
                row.append(self.getTileByNoise(noise_value))
            tiles.append(row)
        return tiles

    def getTileByNoise(self, noise_value):
        if noise_value < -0.1:
            color = (0, 0, 255)  # 물
        elif noise_value < 0.1:
            color = (34, 139, 34)  # 평지
        else:
            color = (136, 69, 19)  # 산  # 디버깅 출력
        return color

    def draw(self, screen, offset_x, offset_y):
        for i, row in enumerate(self.tiles):
            for j, tile in enumerate(row):
                x = self.world_x + i * self.tile_size + offset_x
                y = self.world_y + j * self.tile_size + offset_y
                pygame.draw.rect(screen, tile, (x, y, self.tile_size, self.tile_size))


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
        current_chunk_x = int(-offset_x) // (self.chunk_size * self.tile_size)
        current_chunk_y = int(-offset_y) // (self.chunk_size * self.tile_size)

        for dx in range(0, 3):
            for dy in range(0, 3):
                chunk = self.get_chunk(current_chunk_x + dx, current_chunk_y + dy)
                chunk.draw(screen, offset_x, offset_y)