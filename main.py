import pygame
from lib.user_input import *
from lib.player import *

uni = 40


class App():


    def __init__(self):
        self.running = True # when this is set to false, the program ends
        sizemod = 1
        self.size = self.width, self.height = int(1200*sizemod), int(800*sizemod)
        self.tile = self.width / 30

        pygame.init()

        self.display_surf = pygame.display.set_mode(self.size)

        self.icon_surf = pygame.image.load("data/textures/logo.ico")
        self.icon_surf.convert_alpha()
        pygame.display.set_caption("Medieval Rescue")
        pygame.display.set_icon(self.icon_surf)

        # temporary font
        self.font = pygame.font.SysFont("lucidaconsole", 16, True)

        self.clock = pygame.time.Clock()

        global uni


    def loop(self):
        map = pygame.image.load("data/textures/maps/C3.png").convert()
        spritemap = pygame.image.load("data/textures/32x32.png").convert()
        self.display_surf.fill((0,0,0))
        self.display_surf.blit(map, (0,0))
        self.display_surf.blit(
            spritemap, (thePlayer.xpos*self.tile, thePlayer.ypos*self.tile),
            (0*32, 53*32, 32, 32)
        )
        pygame.display.flip()

        inputter.key_input(self, thePlayer)

        self.clock.tick(30)


    def on_exit(self):
        pygame.quit()


    def on_execute(self):
        while self.running:
            self.loop()
        self.on_exit()


if __name__ == "__main__":
    theApp = App()
    inputter = User_input(pygame)
    thePlayer = Player()
    theApp.on_execute()
