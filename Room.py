from GameObject import GameObject

class Room(GameObject):
    def __init__(self, name, desc, inside = None, flags = None, synonyms = None, capacity = 0):
        super().__init__(name, desc, inside, flags, synonyms, capacity)
        self.directions = {"north":None, "South":None, "East":None, "West":None, "Up": None, "Down":None}
        
    def add_direction(self,direction,passage):
        self.directions[direction] = passage