from GameObject import GameObject

class Room(GameObject):
    def __init__(self, desc, inside = None, flags = None, actions = None, synonyms = None, capacity = 0):
        super().__init__(desc, inside, flags, actions, synonyms, capacity)
        self.directions = {"north":None, "South":None, "East":None, "West":None, "Up": None, "Down":None}
        
