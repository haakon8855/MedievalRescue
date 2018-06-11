import json


class Renderer():


	def __init__(self, pygame):
		self.pygame = pygame
		self.spritemap = self.pygame.image.load("data/textures/32x32.png")
		with open("data/src.json", "r") as src_file:
			self.map_src = json.load(src_file)


	def render(self, app, player):
		if app.need_new_map:
			src = self.map_src[player.current_map]
			self.map = self.pygame.image.load(src)
			# self.map = self.pygame.image.load("data/textures/maps/C3.png")
			app.need_new_map = False

		app.display_surf.fill(app.color["black"])
		app.display_surf.blit(self.map, (0,0))
		app.display_surf.blit(
			self.spritemap, (player.xpos*app.tile, player.ypos*app.tile),
			(0*32, 53*32, 32, 32)
		)

		self.pygame.display.flip() # sets the changes into effect


	def move_anim(self, app, player, axis, direction):
		speed = 2
		if player.sprint:
			speed *= 2

		if axis == 0:
			modifiers = [1,0]
		elif axis == 1:
			modifiers = [0,1]

		for i in range(int(app.tile)):
			if i % speed != 0:
				continue
			adderx = i * modifiers[0] * direction
			addery = i * modifiers[1] * direction
			app.display_surf.fill(app.color["black"])
			app.display_surf.blit(self.map, (0,0))
			app.display_surf.blit(
				self.spritemap,
				(player.xpos*app.tile+adderx, player.ypos*app.tile+addery),
				(0*32, 53*32, 32, 32)
			)
			self.pygame.display.flip()

		if axis == 0:
			player.xpos += 1 * direction
		elif axis == 1:
			player.ypos += 1 * direction
