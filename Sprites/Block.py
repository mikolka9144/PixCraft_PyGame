import pygame
from pygame import Surface

import Config
from Sprites.Sprite import PixSprite
from pygame.math import Vector2
from multipledispatch import dispatch

class BlockDescriptor:
    def __init__(self, texture: Surface):
        self.texture = texture


class Block(PixSprite):
    @dispatch(int, int, BlockDescriptor)
    def __init__(self, BlockX, BlockY, descriptor: BlockDescriptor):
        self.__init__(Vector2(BlockX * Config.SIZE, BlockY * Config.SIZE),descriptor)

    @dispatch(Vector2, BlockDescriptor)
    def __init__(self, vector:Vector2, descriptor: BlockDescriptor):
        scaled_texture = pygame.transform.scale(
            descriptor.texture, (Config.SIZE, Config.SIZE)
        )
        super(Block, self).__init__(
            Vector2(vector.x, vector.y), scaled_texture
        )
