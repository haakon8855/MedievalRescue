import pygame
from pygame.locals import *
from lib.user_input import *
from lib.player import *
from lib.renderer import *

# husk å fjerne:
#	* player.obst_save

color = {
	"black": (0,0,0),
	"white": (255, 255, 255)
}


class App():


	def __init__(self, color):
		self.running = True # when this is set to false, the program ends
		self.color = color
		pygame.init()

		sizemod = 1
		self.width, self.height = int(1200*sizemod), int(800*sizemod)
		self.size = self.width, self.height
		self.display_surf = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Medieval Rescue")
		self.icon_surf = pygame.image.load("data/textures/logo.png")
		# self.icon_surf.convert()
		pygame.display.set_icon(self.icon_surf)
		# temporary font
		self.font = pygame.font.SysFont("lucidaconsole", 16, True)

		self.clock = pygame.time.Clock()

		self.tile = self.width / 30
		self.need_new_map = True


	def loop(self):
		inputter.key_input(self, thePlayer, theRenderer)
		theRenderer.render(self, thePlayer)
		self.clock.tick(30)


	def on_exit(self):
		pygame.quit()


	def on_execute(self):
		while self.running:
			self.loop()
		self.on_exit()


if __name__ == "__main__":
	theApp = App(color)
	inputter = User_input(pygame)
	thePlayer = Player()
	theRenderer = Renderer(theApp, pygame)
	theApp.on_execute()
