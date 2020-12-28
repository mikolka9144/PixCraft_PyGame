import random
from typing import List

from Sprites.Block import Block
from StaticBlocksDescriptions import Block_types as ID
#################
class Noise:
    def __init__(self, minHeight, maxHeight):
        self.minHeight = minHeight
        self.maxHeight = maxHeight
        self.current = 3

    def generateNext(self):
        num = random.randint(-1, 1)
        self.current += num
        if self.current < self.minHeight:
            self.current = self.minHeight
        elif self.current > self.maxHeight:
            self.current = self.maxHeight
        return self.current


#################
class Generator:
    def __init__(self, noise, noise2, world:List):
        self.noise = noise
        self._world = world
        self.dirt_noise = noise2
        self.CanGenerateTree = 0

    def Generate(self, blocks):
        self.GenerateTerrian(blocks)

    def GenerateTerrian(self, blocks):
        for i in range(-blocks, blocks):
            num = self.noise.generateNext()
            dirtSize = self.dirt_noise.generateNext()
            for j in range(num, num - dirtSize, -1):
                self.GenerateFillarOfDirt(j, i, num)
            self.GenerateStoneCollumn(i, num - dirtSize)

    def GenerateFillarOfDirt(self, BlockY, BlockX, num):
        if num == BlockY:
            self._world.append(Block(BlockX, BlockY, ID[1]))
            if random.randint(0, 4) == 3 and num >= 3 and self.CanGenerateTree == 3:
                self.GenerateTree(BlockX, BlockY)
            elif self.CanGenerateTree != 3:
                self.CanGenerateTree += 1
        else:
            self._world.append(Block(BlockX, BlockY, ID[2]))

    def GenerateTree(self, X, Y):
        for i in range(Y + 1, Y + 4):
            self._world.append(Block(X, i, ID[4]))
        self._world.append(Block(X, (Y + 4), ID[5]))
        self._world.append(Block((X - 1), (Y + 3), ID[5]))
        self._world.append(Block((X + 1), (Y + 3), ID[5]))
        self.CanGenerateTree = 0

    def GenerateStoneCollumn(self, x, startI):
        for y in range(startI, -15, -1):
            self._world.append(Block(x, y, ID[3]))
