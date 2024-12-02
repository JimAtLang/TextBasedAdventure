class Obstacle:
    def __init__(self, closed_message, open_commands, key, open = False):
        self.closed_message = closed_message
        self.open_commands = open_commands
        self.key = key
        self.open = open

