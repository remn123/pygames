import pygame, sys

from factory import Factory
from ui import Background, Button
from window import Window
from concepts import Creatable

class Game(Creatable):

    def __init__(self, *args, **kwargs):

        self.clock_ = None
        self._build(**kwargs)

    
    def _build_dict(self, list_):
        for l in list_:
            alias, value = l.popitem()
            if isinstance(value, dict):
                type_ = value.pop("type", None)
                if type_ is not None:
                    yield {f'{alias}': Factory.make(type_, value)}
                else:
                    yield {f'{alias}': value}
            else:
                yield {f'{alias}': value}


    def _build(self, *args, **kwargs):
        for item in kwargs.items():
            alias, value = item
            if isinstance(value, dict):
                type_ = value.pop("type", None)
                if type_ is not None:
                    self.__setattr__(alias, Factory.make(type_, value))
                else:
                    self.__setattr__(alias, value)
            elif isinstance(value, list):
                aliasdict = dict()
                for n in self._build_dict(value):
                    aliasdict.update(n)
                self.__setattr__(alias, aliasdict)
            else:
                self.__setattr__(alias, value)
        
        
    def __setattr__(self, alias, value):
        self.__dict__[alias]=value


    def setup(self):
        print(f"Setting up window...")
        self.window.setup()
        print(f"Window ok!")

        for key in self.ui.keys():
            print(f"Setting up {key}.")
            self.ui[key].setup()
            print(f"{key} ok!")

        self.clock_ = pygame.time.Clock()
        # for key in self.assets.keys():
        #     self.ui[key].setup()

    def clock(self):
        self.clock_.tick(self.tick)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
            # if event.type == pygame.KEYDOWN: 
            #     if event.key == pygame.K_RIGHT:
            #         x += 5
            #     if event.key == pygame.K_LEFT:
            #         x -= 5
            #     if event.key == pygame.K_DOWN:
            #         y += 5
            #     if event.key == pygame.K_UP:
            #         y -= 5

    def update(self):
        self.window.update()

    def render(self):
        for key in self.ui.keys():
            #print(f"Rendering {key}...")
            self.window.render(self.ui[key])

