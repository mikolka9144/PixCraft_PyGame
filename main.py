import Engine
from SpecialSprites import MouseSprite,MousePointer
from Sprites import Player

from Generator import Generator,Noise

MainEngine = Engine.GameEngine()
noise1 = Noise(1,5)
noise2 = Noise(2,5)
generator = Generator(noise1,noise2,MainEngine.all_sprites[Engine.BLOCKS])
generator.Generate(300)
mouse = MouseSprite.Mouse()
MainEngine.all_sprites[Engine.SPECIAL].append(mouse)
MainEngine.all_sprites[Engine.SPECIAL].append(MousePointer.MousePointer(mouse,MainEngine.all_sprites[Engine.BLOCKS]))
MainEngine.move_camera(220,90)
P1 = Player.Player(GameEngine=MainEngine)

MainEngine.all_sprites[Engine.ENTITIES].append(P1)
MainEngine.start()
