from obj.obj import Obj
from obj.tile import Tile
from draw.drawable import Circle
import pygame, sys

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
bgc = (0, 0, 0)

Tester = Tile((20,100), (50, 50))
Tester2 = Tile((200,100), (50, 50))
Tester.setFace(Circle())
print(Tester.getArea());

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit();
	
	screen.fill(bgc)
	screen.blit(Tester2.draw(), Tester2.pos)
	screen.blit(Tester.draw(), Tester.pos)
	pygame.display.flip()