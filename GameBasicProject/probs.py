import pygame
import globs

class Text:
    def __init__(self, text: str, font: str):
        self.string = text
        self.font = font

        self.textFont = pygame.font.SysFont(font, 50)
        self.text = self.textFont.render(text, True, globs.white)

        self.rect = self.text.get_rect()

    def draw(self, screen:pygame.display, x: int, y: int):
        self.rect.center = (x, y)
        screen.blit(self.text, self.rect)

class Image:
    def __init__(self, src: str):
        self.src = src
        self.imageObj = pygame.image.load(src)
