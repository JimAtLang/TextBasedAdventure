from Directions import Directions


class Passage:
    def __init__(self, from_room, to_room, from_dir, custom_from_dir=None, custom_to_dir=None, obstacle = None):
        if not from_room[from_dir]:
            from_room.add_direction(from_dir, self)
        else:
            raise ValueError("The direction " + from_dir.value + " is already assigned in room " + from_room.name)

        self.from_room = from_room
        self.to_room = to_room
        if not isinstance(from_dir, Directions):
            raise TypeError("Use NORTH, SOUTH, EAST, WEST, UP, DOWN for directions, or to use custom directions use from_dir = CUSTOM and custom_from_direction, custom_to_direction to assign")
        if from_dir == Directions.CUSTOM:
            if not custom_from_dir or not custom_to_dir:
                raise  TypeError("for CUSTOM directions include custom_from_dir argument and custom_to_dir argument")
        self.from_dir = from_dir
        if from_dir == Directions.NORTH:
            self.to_dir = Directions.SOUTH
        elif from_dir == Directions.SOUTH:
            self.to_dir = Directions.NORTH
        elif from_dir == Directions.EAST:
            self.to_dir = Directions.WEST
        elif from_dir == Directions.WEST:
            self.to_dir = Directions.EAST
        elif from_dir == Directions.UP:
            self.to_dir = Directions.DOWN
        else: # from_dir = DOWN
            self.to_dir = Directions.UP
        if not self.to_room[self.to_dir]:
            self.to_room.add_direction(self.to_dir, self)
        else:
            raise ValueError("The direction " + self.to_dir.value + " is already assigned in room " + to_room.name)

        self.obstacle = obstacle