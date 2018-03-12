from obj.obj import Obj
from draw.drawable import Drawable
from pygame import Surface
from draw import imgconsts

class	Tile (Obj):
	def __init__(self, pos, size):
		Obj.__init__(self, pos)
		self.size = size
		self.face = Drawable()
		
	def	setFace(self, face :Drawable):
		self.face = face;
		
	def draw(self):
		if self.face != None:
			surf = imgconsts.getSurface(self.size)
			self.face.draw(surf);
			return surf
		return None
		
	def getArea(self):
		return (*self.pos, *self.size)
		
class	TileContainer (Tile):
	def __init__(self, pos, size):
		Tile.__init__(self, pos, size)
		self.children = []
		self.face.color = (255, 0, 0, 255)
	
	def addTile(self, child :Tile):
		self.children.append(child);
	
	def draw(self):
		surf = Tile.draw(self)
		if (surf != None):
			for child in self.children:
				csurf = child.draw()
				csurf.convert_alpha(surf)
				surf.blit(csurf, child.pos)
			return surf
		return None