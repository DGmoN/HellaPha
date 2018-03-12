from pygame import Surface

def getSurface(size):
	surf = Surface(size)
	surf.set_alpha(255);
	surf.set_colorkey((0, 0, 0, 255))
	surf.fill((0, 0, 0, 255));
	return surf