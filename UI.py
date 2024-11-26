from Parser import Parser
from World import World

class UI:
    def __init__(self):
        self.parser = Parser()
        self.World = World()
        self.game_loop()

    def game_loop(self):
        while True:
            move = input()
            self.parser.parse(move)

    def say(self,string):
        print(string)