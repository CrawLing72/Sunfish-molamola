from contextlib import nullcontext
import pygame
from pygame.examples.midi import NullKey


class Text:
    def __init__(self, text: str, font: str, textsize: int, color: tuple):
        self.string = text
        self.font = font
        self.color = color

        self.textFont = pygame.font.Font(font, textsize)
        self.text = self.textFont.render(self.string, True, color)

        self.rect = self.text.get_rect()

    def draw(self, screen:pygame.display, x: int, y: int):
        self.text = self.textFont.render(self.string, True, self.color)
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

    def adjust(self, x: int, y: int):
        self.imageObj = pygame.transform.scale(self.imageObj, (x, y))


class Button:
    def __init__(self, imgsrc:str, evnetfunc: object = None):
        self.src = imgsrc
        self.img = pygame.image.load(self.src)
        self.rect = self.img.get_rect()
        self.func = evnetfunc

    def draw(self, x: int, y: int, screen: pygame.display):
        self.rect.center = (x, y)

        screen.blit(self.img, self.rect)

    def detection(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.rect.x <= mouse[0] <= self.rect.x + self.rect.width and self.rect.y <= mouse[1] <= self.rect.y + self.rect.height:
            if click[0]:
                self.func()


class Character:
    def __init__(self, imgsrc:dict, target_fps:int, x:int, y:int):
        self.imagedict = imgsrc
        self.imgsrc = []
        self.target_seconds = target_fps
        self.x = x
        self.y = y
        self.animation_index = 0
        self.actual_seconds = 0


    def decision_src (self, x_offset:int, y_offset:int):
        if(x_offset < 0):
            self.imgsrc = self.imagedict["a"]
        elif (x_offset > 0):
            self.imgsrc = self.imagedict["d"]
        elif(y_offset < 0):
            self.imgsrc = self.imagedict["s"]
        elif (y_offset > 0):
            self.imgsrc = self.imagedict["w"]
        else:
            self.imgsrc = self.imagedict["e"]

    def draw(self, screen:pygame.display, x_dist: int, y_dist: int, deltatime:float):
        self.decision_src(x_dist, y_dist)

        self.actual_seconds += deltatime

        if (self.actual_seconds > self.target_seconds):
            self.actual_seconds = 0
            if self.animation_index < (len(self.imgsrc) - 1):
                self.animation_index += 1
            else:
                self.animation_index = 0

        if(self.animation_index > len(self.imgsrc) - 1):
            self.animation_index = 0

        self.imgsrc[self.animation_index].draw(screen, self.x, self.y)



