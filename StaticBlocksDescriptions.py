import pygame

from Sprites.Block import BlockDescriptor

Block_types = []

Block_types.append(None)
Block_types.append(BlockDescriptor(pygame.image.load("grass.png")))
Block_types.append(BlockDescriptor(pygame.image.load("dirt.png")))
Block_types.append(BlockDescriptor(pygame.image.load("stone.png")))
Block_types.append(BlockDescriptor(pygame.image.load("wood.png")))
Block_types.append(BlockDescriptor(pygame.image.load("leaves.jpg")))
