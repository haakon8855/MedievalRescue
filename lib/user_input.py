class User_input():


    def __init__(self, pygame):
        self.pygame = pygame


    def key_input(self, app, player):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                app.running = False
            # the following runs if a key is pressed
            elif event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_ESCAPE:
                    app.running = False
                elif event.key == self.pygame.K_UP:
                    player.ypos -= 1
                elif event.key == self.pygame.K_DOWN:
                    player.ypos += 1
                elif event.key == self.pygame.K_LEFT:
                    player.xpos -= 1
                elif event.key == self.pygame.K_RIGHT:
                    player.xpos += 1
