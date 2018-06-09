import pygame
from lib.user_input import *

uni = 40


class App():


    def __init__(self):
        self.running = True # when this is set to false, the program ends
        self.size = self.width, self.height = 1200, 800

        pygame.init()

        self.display_surf = pygame.display.set_mode(self.size)

        self.icon_surf = pygame.image.load("data/textures/logo.ico")
        pygame.display.set_caption("Medieval Rescue")
        pygame.display.set_icon(self.icon_surf)

        # temporary font
        self.font = pygame.font.SysFont("lucidaconsole", 16, True)

        self.clock = pygame.time.Clock()

        global uni


    def loop(self):
        # print("hello")
        map = pygame.image.load("data/textures/maps/C3.png").convert()
        man = pygame.image.load("data/textures/logo.ico").convert()
        # imagerect = map.get_rect()
        self.display_surf.fill((0,0,0))
        self.display_surf.blit(map, (0,0))
        self.display_surf.blit(man, (10*uni, 15*uni))
        pygame.display.flip()
        self.clock.tick(30)

        inputter.key_input(self)


    def on_exit(self):
        pygame.quit()


    def on_execute(self):
        while self.running:
            self.loop()
        self.on_exit()


if __name__ == "__main__":
    theApp = App()
    inputter = User_input(pygame)
    theApp.on_execute()
