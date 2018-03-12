class Obj:
	def	__init__(self):
		self.pos = (0, 0)
		
	def __init__(self, pos):
		self.pos = pos;
		
	def get_position(self):
		return self.pos
		
	def set_position(self, pos):
		self.pos = pos
		