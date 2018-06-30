class Player():


	def __init__(self):
		self.current_map = 12
		self.xpos = 10
		self.ypos = 10
		self.sprint = False
		self.obst_save = []


	def obst_creator(self, mode):
		if mode == 0:
			self.obst_save.append([self.xpos, self.ypos])
		elif mode == 1:
			print(self.obst_save)
		elif mode == 2:
			self.obst_save = []
