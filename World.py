from Player import Player
from Room import Room
from Verb import Verb
from UI import UI
class World:
    def __init__(self):
        self.player = Player(Room("Empty room"))
        self.verbs = [Verb("go", self.player.location)]
        self.ui = UI()

    def act(self, verb, io, do):
        pass

    def go(self, direction):
        if self.player.location[direction]:
            self.player.location = self.player.location[direction]
            self.ui.say(self.player.location.desc)
        else:
            self.ui.say("You can't go there")