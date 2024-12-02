from DeadEnd import DeadEnd


class Actions:
    def __init__(self, player, world, ui):
        self.player = player
        self.world = world
        self.ui = ui
    def go(self, direction):
        if self.player.location[direction]:
            passage = self.player.location[direction]
            if isinstance(passage, DeadEnd):
                self.ui.say(passage.desc)
                return
            if passage.obstacle and not passage.obstacle.open:
                self.ui.say(passage.obstacle.closed_message)
            else:
                if self.player.location == passage.from_room:
                    self.player.location = passage.to_room
                else:
                    self.player.location = passage.to_room
        else:
            self.ui.say("You can't go there")

    def open_obstacle(self, verb, io, obstacle):
        if verb in obstacle.open_commands and io == obstacle.key:
            self.ui.say(obstacle.open_message)
        else:
            self.ui.say("You can't " + verb + " the " + obstacle.desc + " with a " + io)
