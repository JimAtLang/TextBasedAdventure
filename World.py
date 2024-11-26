from Player import Player
from Room import Room
class World:
    def __init__(self):
        self.player = Player(Room("Empty room"))
        self.verbs = ["go"]