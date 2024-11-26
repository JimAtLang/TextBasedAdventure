from GameObject import GameObject

class Room(GameObject):
    def __init__(self, desc, inside = None, flags = None, actions = None, synonyms = None, capacity = 0, north=None, south=None, east=None, west=None, up=None, down=None):
        super().__init__(desc, inside, flags, actions, synonyms, capacity)
        self.north = north
        self.west = west
        self.east = east
        self.south = south
        self.up = up
        self.down = down
        
