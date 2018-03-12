from obj.obj import Obj
from draw.drawable import Drawable
from pygame import Surface

class	Tile (Obj):

	def __init__(self, pos, size):
		Obj.__init__(self, pos)
		self.size = size
		self.face = Drawable()
		
	def	setFace(self, face :Drawable):
		self.face = face;
		
	def draw(self):
		if self.face != None:
			surf = Surface(self.size);
			self.face.draw(surf);
			return surf
		return None
		
	def getArea(self):
		return (*self.pos, *self.size)