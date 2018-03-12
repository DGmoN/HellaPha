import pygame
from pygame import Surface
from pygame import draw
from pygame import gfxdraw

class	Drawable:
	def	__init__(self):
		self.color = (255, 255, 255, 255)
		pass
		
	def draw(self, surf :Surface):
		draw.rect(surf, self.color, surf.get_rect(), 5)
		pass
		
class	Circle(Drawable):
	def	draw(self, surf :Surface):
		center = (int(surf.get_width()/2), int(surf.get_height()/2))
		gfxdraw.filled_circle(surf, center[0], center[1], center[0] - 2, self.color)
		gfxdraw.aacircle(surf, center[0], center[1], center[0] - 2, self.color)