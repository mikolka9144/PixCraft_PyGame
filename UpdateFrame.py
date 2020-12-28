import pygame

import Config

clock = pygame.time.Clock()


def do_update(engine):

    if Config.DEBUG_UPDATES:
        do_debug_update(engine)
    else:
        do_normal_update(engine)


def do_debug_update(engine):
    if not pygame.key.get_pressed()[pygame.K_l]:
        do_normal_update(engine)
        debug_update_passed = False
        return
    for entity in engine.all_sprites.values():
        for sprite in entity:
            if sprite.force_update or engine.IsRenderable(sprite.rect):
                clock.tick()
                sprite.update()
                clock.tick()
                print(f"update for {type(sprite)} took {clock.get_time()}")
                if sprite.surf is not None:
                    engine.displaysurface.blit(sprite.surf, sprite.rect)
    print("-"*30)


def do_normal_update(engine):
    for entity in engine.all_sprites.values():
        for sprite in entity:
            if sprite.force_update or engine.IsRenderable(sprite.rect):
                sprite.update()
                if sprite.surf is not None:
                    engine.displaysurface.blit(sprite.surf, sprite.rect)
