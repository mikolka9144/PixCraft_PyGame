import pygame

import Config
import Engine
from pygame.math import Vector2 as vector

from Sprites.Sprite import PixSprite


class Player(PixSprite):
    def __init__(self, GameEngine):
        self._engine: Engine.GameEngine = GameEngine
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((128, 255, 40))
        super(Player, self).__init__(vector(0, 0), self.surf)
        self.speed = 0
        self.FallDistance = 0
        self.Grounded = True

    def update(self):
        keyboard_state = pygame.key.get_pressed()
        self.process_vertical_movement(keyboard_state)

        self.process_jump(keyboard_state)
        for block in self._engine.all_sprites[Engine.BLOCKS]:
            if self.collide(block):
                if block.position.y > 0:
                    if self.speed > 0:
                        self.speed = -self.speed
                elif block.position.y <= Config.GROUND_BLOCK_OFFSET:
                    self._ground_player()

        self.process_falling_and_fall_damage()

    def process_jump(self, keyboard_state):
        if keyboard_state[pygame.K_SPACE] and self.Grounded:
            self.Grounded = False
            self.speed = Config.PLAYER_JUMP_SPEED

    def process_vertical_movement(self, keyboard_state):
        if keyboard_state[pygame.K_d]:
            self.flip = True
            self.move_player(Config.WALKING_SPEED, 0)
            for block in self._engine.all_sprites[Engine.BLOCKS]:
                if self.collide(block) and block.position.y >= Config.BLOCK_MIN_HEIGHT_TO_THREAT_AS_WALL:
                    self.move_player(Config.WALKING_SPEED, -180)
                    break
        elif keyboard_state[pygame.K_a]:
            self.flip = False
            self.move_player(Config.WALKING_SPEED, -180)
            for block in self._engine.all_sprites[Engine.BLOCKS]:
                if self.collide(block) and block.position.y >= Config.BLOCK_MIN_HEIGHT_TO_THREAT_AS_WALL:
                    self.move_player(Config.WALKING_SPEED, 0)
                    break

    def process_falling_and_fall_damage(self):
        if self.speed != 0:
            self.move_player(self.speed, 90)
            if self.speed < 0:
                self.FallDistance -= self.speed
        if self.speed > Config.FALL_SPEED_CAP:
            self.speed = self.speed + Config.FALL_SPEED_CHANGE

    def move_player(self, dist, rot):
        self._engine.move_camera(dist, rot)
        self.move(dist, rot)

    def _ground_player(self):
        self.Grounded = True
        self.FallDistance = 0
        if self.speed < 0:
            self.speed = 0
