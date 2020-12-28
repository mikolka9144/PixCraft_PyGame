from pygame.math import Vector2

from Sprites.Sprite import PixSprite


class SpecialSprite(PixSprite):
    def __init__(self,pos:Vector2,rect):
        super().__init_subclass__()
        self.rect = rect
        self.force_update = True
        self.position = pos
        self.surf = None