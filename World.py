from Player import Player
from Room import Room
from Verb import Verb
class World:
    def __init__(self):
        self.player = Player(Room("Empty room"))
        self.verbs = [Verb("go", self.player.location)]

    def act(self, verb, io, do):
        pass