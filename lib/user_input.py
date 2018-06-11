class User_input():


	def __init__(self, pygame):
		self.pygame = pygame
		self.pygame.key.set_repeat(500, 30)


	def key_input(self, app, player, renderer):
		for event in self.pygame.event.get():
			if event.type == self.pygame.QUIT:
				app.running = False
			# the following runs if a key is pressed
			if event.type == self.pygame.KEYDOWN:
				if event.key == self.pygame.K_LSHIFT:
					player.sprint = True
			if event.type == self.pygame.KEYUP:
				if event.key == self.pygame.K_LSHIFT:
					player.sprint = False

		keys = self.pygame.key.get_pressed()
		if keys[self.pygame.K_ESCAPE]:
			app.running = False
		elif keys[self.pygame.K_UP]:
			renderer.move_anim(app, player, 1, -1)
			if player.ypos < 0:
				player.ypos = 19
				player.current_map -= 5
				app.need_new_map = True
		elif keys[self.pygame.K_DOWN]:
			renderer.move_anim(app, player, 1, 1)
			if player.ypos > 19:
				player.ypos = 0
				player.current_map += 5
				app.need_new_map = True
		elif keys[self.pygame.K_LEFT]:
			renderer.move_anim(app, player, 0, -1)
			if player.xpos < 0:
				player.xpos = 29
				player.current_map -= 1
				app.need_new_map = True
		elif keys[self.pygame.K_RIGHT]:
			renderer.move_anim(app, player, 0, 1)
			if player.xpos > 29:
				player.xpos = 0
				player.current_map += 1
				app.need_new_map = True
