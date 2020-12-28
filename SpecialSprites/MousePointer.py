import math

import pygame
from pygame import Rect
from pygame.math import Vector2

import Config
import StaticBlocksDescriptions as blocks_types
from SpecialSprites import MouseSprite
from SpecialSprites.SpecialSprite import SpecialSprite
from Sprites.Block import Block


class MousePointer(SpecialSprite):
    def __init__(self,mouse:MouseSprite,BlocksList:list):
        super().__init__(Vector2(0,0),Rect(0, 0,Config.SIZE,Config.SIZE))
        self.blocks_list = BlocksList
        self.mouse = mouse
        self.surf = pygame.surface.Surface((Config.SIZE, Config.SIZE))
        self.surf.fill((100, 200, 50))

    def update(self):
        self.update_pointer_position()
        mouse_state = pygame.mouse.get_pressed(3)
        if mouse_state[0]:
            if not self.is_block_selected():
                self.blocks_list.append(Block(self.position,blocks_types.Block_types[2]))
        elif mouse_state[2]:
            for block in self.blocks_list:
                if block.position == self.position:
                    self.blocks_list.remove(block)
                    break

    def is_block_selected(self):
        for block in self.blocks_list:
            if block.position == self.position:
                return True
        return False

    def update_pointer_position(self):
        x_diff = self.mouse.position.x - self.position.x
        y_diff = self.mouse.position.y - self.position.y
        block_border = Config.SIZE / 2
        x_units_to_move = math.ceil(x_diff / block_border)
        y_units_to_move = math.ceil(y_diff / block_border)

        x_to_move = math.floor(x_units_to_move / 2) * Config.SIZE
        y_to_move = math.floor(y_units_to_move / 2) * Config.SIZE

        current_position = self.position
        self.position = Vector2(current_position.x + x_to_move, current_position.y + y_to_move)

