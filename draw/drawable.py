import pygame
from pygame import Surface
from pygame import draw

class	Drawable:
	def	__init__(self):
		pass
		
	def draw(self, surf :Surface):
		draw.rect(surf, (255, 255, 255), surf.get_rect())
		pass
		
class	Circle(Drawable):
	def	draw(self, surf :Surface):
		center = (int(surf.get_width()/2), int(surf.get_height()/2))
		draw.circle(surf, (255, 255, 255), center, center[0])