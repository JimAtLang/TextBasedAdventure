from Player import Player
from Room import Room
from Verb import Verb
from UI import UI
class World:
    def __init__(self):
        self.player = Player(Room("Empty room"))
        self.verbs = [Verb("go", self.player.location)]
        self.ui = UI()

    def find_verb(self, verb_string):
        for verb in self.verbs:
            if verb.name == verb_string:
                return verb
            else:
                return None

    def act(self, verb_string, io, do):
        verb = self.find_verb(verb_string)
        if verb:
            pass
        else:
            self.ui.say("I don't know how to " + verb_string)


    def go(self, direction):
        if self.player.location[direction]:
            self.player.location = self.player.location[direction]
            self.ui.say(self.player.location.desc)
        else:
            self.ui.say("You can't go there")