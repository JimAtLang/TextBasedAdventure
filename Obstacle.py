class Obstacle:
    def __init__(self, name, desc, closed_message, open_message, open_commands, key, open = False):
        self.name = name
        self.desc = desc
        self.closed_message = closed_message
        self.open_message = open_message
        self.open_commands = open_commands
        self.key = key
        self.open = open

