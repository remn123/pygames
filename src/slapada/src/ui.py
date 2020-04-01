import pygame

from config import Config
from concepts import Creatable

class UserInterface(Creatable):

    def __init__(self, *args, **kwargs):
        self.status = None
        self.count = -1
        self.index = 0
        
        for tuple_ in kwargs.items():
            key, value = tuple_
            self.__setattr__(key, value)

    def __setattr__(self, key, value):
        print(f"Setting new attribute '{key}' inside {self.__class__} with value = {value}...")
        self.__dict__[key]=value
        print(f"{key}= {self.__dict__[key]}")

    def _load_frame(self, path):
        return pygame.transform.scale(pygame.image.load(path), self.get_size())

    def _cycles(self):
        return len(self.images[self.status]["frame"])

    def setup(self):
        for key in self.images.keys():
            print(f"[{self.__class__}]: Loading frames for status = {key}")
            self.images[key].update({"frame": [self._load_frame(i) for i in self.images[key]['path']]})

    def get_position(self):
        position = self.dynamics["position"]
        return tuple(position.values())

    def get_status(self):
        return self.status, self.index

    def get_frame(self):
        status, index = self.get_status()
        return self.images[status]["frame"][index]

    def get_size(self):
        return tuple([self.width, self.height])

    def update(self):
        if self.dynamics["type"] == 'static':
            self.count += 1
            self.index = 0
            # if self.count % self.tick == 0:
            #     self.index += 1 
            #     self.index = self.index % self._cycles()

    def event(self):
        pass

class Background(UserInterface, Creatable):

    def __init__(self, *args, **kwargs):
        super().__init__(self, **kwargs)
        self.status = "idle"

    

class Button(UserInterface, Creatable):

    def __init__(self, *args, **kwargs):
        super().__init__(self, **kwargs)
        self.status = "idle"
