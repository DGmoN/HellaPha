import pygame

pygame.init()

width = 500
height = 500
size = (width,height)
bgcolour = (0,0,0)
resizeable = False


pygame.display.set_caption('Alpha 0.1')
screen = pygame.display.set_mode(size)
screen.fill(bgcolour)




running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()
