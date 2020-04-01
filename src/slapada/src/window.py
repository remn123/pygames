import pygame

from config import Config
from concepts import Creatable

class WindowInterface(Creatable):

    def __init__(self, *args, **kwargs):
        self.screen = None

        for tuple_ in kwargs.items():
            key, value = tuple_
            self.__setattr__(key, value)

    def __setattr__(self, key, value):
        self.__dict__[key]=value


class Window(WindowInterface, Creatable):

    def __init__(self, *args, **kwargs):
        super().__init__(self, **kwargs)
        
    def setup(self):
        self.screen = pygame.display.set_mode(self.get_size())

    def render(self, obj: Creatable):
        self.screen.blit(obj.get_frame(), obj.get_position())

    def update(self):
        #self.screen.fill((0, 0, 0))
        pygame.display.update()

    def get_size(self):
        return tuple([self.width, self.height])
