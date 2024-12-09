from GameObject import GameObject
from Actions import Actions

class Room(GameObject):
    def __init__(self, name, desc, contains = None, flags = None, synonyms = None, capacity = 0):
        super().__init__(name, desc, contains, flags, synonyms, capacity)
        self.directions = {"north":None, "South":None, "East":None, "West":None, "Up": None, "Down":None}
        self.actions.add("go", Actions.go)
        self.actions.add("look", Actions.look)
        
    def add_direction(self,direction,passage):
        self.directions[direction] = passage