from Parser import Parser

class UI:
    def __init__(self):
        self.parser = Parser()
        self.game_loop()

    def game_loop(self):
        while True:
            move = input()
            self.parser.parse(move)
