import cmath

import pygame
from pygame.math import Vector2 as vector, Vector2
import Config


class PixSprite(pygame.sprite.Sprite):
    def __init__(self,pos:Vector2,surface):
        super().__init__()
        self.rect = surface.get_rect()
        self.force_update = False
        self.position = pos
        self.surf = surface

    def collide(self,sprite):
        IsVisible = self._engine.IsRenderable(sprite.rect)
        return self.rect.colliderect(sprite.rect) and IsVisible

    @property
    def position(self):
        x = self.rect.centerx-(Config.WIDTH/2)
        y = self.rect.centery-(Config.HEIGHT/2)
        return vector(x, -y)

    @position.setter
    def position(self, value):
        x = value.x + (Config.WIDTH / 2)
        y = (Config.HEIGHT / 2) - value.y
        self.rect.center = vector(x, y)
    def move(self, dist, rot):
        multiply = 0.017453292519944
        num = 90.0
        num2 = dist * cmath.sin(multiply * (-rot + num)).real
        num3 = dist * cmath.cos(multiply * (-rot + num)).real
        self.position = vector(self.position.x + int(num2), self.position.y + int(num3))
