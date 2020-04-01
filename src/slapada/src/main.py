import pygame

from concepts import Creatable
from config import Config
from factory import Factory
from game import Game


pygame.init()
pygame.mixer.init()

config = Config() # default: path = "src/config.py"


game = Game(**config.get("game"))

game.setup()

while 1:
    game.clock()

    game.event()

    game.render()

    game.update()

