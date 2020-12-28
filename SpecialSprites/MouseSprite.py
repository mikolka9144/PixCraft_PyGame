import pygame
from pygame import Rect
from pygame.math import Vector2

import Config
from SpecialSprites.SpecialSprite import SpecialSprite
from Sprites.Sprite import PixSprite


class Mouse(SpecialSprite):
    def __init__(self):
        super().__init__(Vector2(0,0),Rect(20,20,Config.MOUSE_BOX_SIZE,Config.MOUSE_BOX_SIZE))
    def update(self):
        mousePos = pygame.mouse.get_pos()
        self.rect.center = (mousePos[0],mousePos[1])
        print(self.position)
