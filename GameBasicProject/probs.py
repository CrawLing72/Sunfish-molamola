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
        self.rect = self.imageObj.get_rect()

    def draw(self, screen:pygame.display, x: int, y: int):
        self.rect.center = (x, y)
        screen.blit(self.imageObj, self.rect)


class Button:
    def __init__(self, imgsrc:str, evnetfunc: object = None):
        self.src = imgsrc
        self.img = pygame.image.load(self.src)
        self.rect = self.img.get_rect()
        self.func = evnetfunc

    def draw(self, x:int, y:int, width: int, height: int, screen: pygame.display):
        self.rect.center = (x, y)
        self.rect.width = width, self.rect.height = height

        screen.blit(self.img, self.rect)

    def detection(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.rect.x <= mouse[0] <= self.rect.x + self.rect.width and self.rect.y <= mouse[1] <= self.rect.y + self.rect.height:
            self.func()