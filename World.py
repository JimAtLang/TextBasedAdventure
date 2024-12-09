from Player import Player
from Room import Room
from Verb import Verb
from UI import UI
class World:
    def __init__(self):
        self.player = Player(Room("Empty room"))
        self.verbs = [Verb("go", self.player.location)]
        self.ui = UI()
        self.map = []

    def find_verb(self, verb_string):
        for verb in self.verbs:
            if verb.name == verb_string:
                return verb
            else:
                return None

    def act(self, verb_string, io, do):
        verb = self.find_verb(verb_string)
        if verb:
            if io in verb.look_in:
                verb.look_in[io]()
            else:
                self.ui.say("I don't see a " + io + " here,")
        else:
            self.ui.say("I don't know how to " + verb_string)
