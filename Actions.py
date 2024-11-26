class Actions:
    def __init__(self, player, world):
        self.player = player
        self.world = world
    def go(self, direction):
        if self.player.location[direction]:
            self.player.location = self.player.location[direction]
            self.ui.say(self.player.location.desc)
        else:
            self.ui.say("You can't go there")