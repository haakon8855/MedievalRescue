import json


class Renderer():


	def __init__(self, app, pygame):
		self.pygame = pygame
		self.spritemap = self.pygame.image.load("data/textures/32x32.png")
		self.show_fps = True
		self.no_ghost_px = int(app.tile/4)
		with open("data/src.json", "r") as src_file:
			self.map_src = json.load(src_file)
		with open("data/obst.json", "r") as obst_file:
			self.obstacles = json.load(obst_file)


	def render(self, app, player):
		if app.need_new_map:
			src = self.map_src[player.current_map]
			self.map = self.pygame.image.load(src).convert()
			# self.map = self.pygame.image.load("data/textures/maps/C3.png")

		# app.display_surf.fill(app.color["black"])
		app.display_surf.blit(self.map, (0,0))
		if app.need_new_map:
			self.pygame.display.update((0,0,app.width, app.height))
		app.display_surf.blit(
			self.spritemap, (player.xpos*app.tile, player.ypos*app.tile),
			(0*32, 53*32, 32, 32)
		)

		if self.show_fps:
			fps = app.clock.get_fps()
			fps_surf = app.font.render(str(fps), False, app.color["white"])
			app.display_surf.blit(fps_surf, (5, 5))

		update_rect = (
			player.xpos*app.tile, player.ypos*app.tile,
			app.tile, app.tile
		)
		self.pygame.display.update(update_rect)

		app.need_new_map = False
		# self.pygame.display.flip() # sets the changes into effect


	def move_anim(self, app, player, axis, direction):
		speed = 2
		if player.sprint:
			speed *= 2

		if axis == 0:
			modifiers = [1,0]
		elif axis == 1:
			modifiers = [0,1]

		for i in range(int(app.tile)):
			adderx = i * modifiers[0] * direction
			addery = i * modifiers[1] * direction
			app.display_surf.fill(app.color["black"])
			app.display_surf.blit(self.map, (0,0))
			app.display_surf.blit(
				self.spritemap,
				(player.xpos*app.tile+adderx, player.ypos*app.tile+addery),
				(0*32, 53*32, 32, 32)
			)
			self.pygame.time.wait(speed)
			update_rect = (
				player.xpos*app.tile+adderx-self.no_ghost_px,
				player.ypos*app.tile+addery-self.no_ghost_px,
				app.tile+2*self.no_ghost_px,
				app.tile+2*self.no_ghost_px
			)
			self.pygame.display.update(update_rect)
			# self.pygame.display.flip()

		if axis == 0:
			player.xpos += 1 * direction
		elif axis == 1:
			player.ypos += 1 * direction


	def legal_move(self, player, axis, direction):
		current_pos = [player.xpos, player.ypos]
		new_pos = [current_pos[0], current_pos[1]]
		new_pos[axis] += direction
		if new_pos in self.obstacles[player.current_map]:
			return False
		return True
