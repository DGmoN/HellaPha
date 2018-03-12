from obj.obj import Obj
from obj.tile import Tile, TileContainer
from draw.drawable import Circle
import pygame, sys

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
screen.convert_alpha();
bgc = (0, 0, 0, 255)
screen.set_alpha(255)
screen.set_colorkey(bgc)
Cont = TileContainer((50, 50), (300, 300))
Tester = Tile((20,100), (50, 50))
Cont.addTile(Tester);
Tester2 = Tile((200,100), (50, 50))
Tester.setFace(Circle())
print(Tester.getArea());

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit();
	
	screen.fill(bgc)
	screen.blit(Tester2.draw(), Tester2.pos)
	screen.blit(Cont.draw(), Cont.pos)
	pygame.display.flip()