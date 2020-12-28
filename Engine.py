import sys
import Config
import pygame


class GameEngine:
    def __init__(self):
        pygame.init()
        self.FramePerSec = pygame.time.Clock()
        self.displaysurface = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption("PixCraft")
        self._create_layers()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.displaysurface.fill((0, 0, 100))

            for entity in self.all_sprites.values():
                for sprite in entity:
                    if self.IsRenderable(sprite.rect) or sprite.force_update:
                        sprite.update()
                        if sprite.surf is not None:
                            self.displaysurface.blit(sprite.surf, sprite.rect)

            pygame.display.update()
            self.FramePerSec.tick(Config.FPS)

    def move_camera(self, dist, rot):
        reverse_rotation = (rot + 180) % 360
        for entity in self.all_sprites.values():
            for sprite in entity:
                sprite.move(dist, reverse_rotation)
        pass

    def _create_layers(self):
        self.all_sprites = {"Blocks": [], "Entities": [], "Special": []}

    def IsRenderable(self, rect):
        left_barrier = Config.BOXLEFT < rect.centerx
        right_barrier = rect.centerx < Config.BOXRIGHT
        up_barrier = Config.BOXUP < rect.centery
        down_barrier = Config.BOXDOWN > rect.centery
        return left_barrier and right_barrier and down_barrier and up_barrier


BLOCKS = "Blocks"
ENTITIES = "Entities"
SPECIAL = "Special"
