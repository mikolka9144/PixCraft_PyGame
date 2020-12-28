import pygame
from pygame import Surface

import Config
from Sprites.Sprite import PixSprite
from pygame.math import Vector2 as vector


class BlockDescriptor:
    def __init__(self, texture: Surface):
        self.texture = texture


class Block(PixSprite):
    def __init__(self, BlockX, BlockY, descriptor: BlockDescriptor):
        scaled_texture = pygame.transform.scale(
            descriptor.texture, (Config.SIZE, Config.SIZE)
        )
        super(Block, self).__init__(
            vector(BlockX * Config.SIZE, BlockY * Config.SIZE), scaled_texture
        )
