from Actions import Actions

class GameObject:
    def __init__(self, name, desc, inside = None, flags = None, synonyms = None, capacity = 0):
        self.name = name
        self.desc = desc
        self.flags = flags
        self.inside = inside
        self.actions = {}
        self.synonyms = synonyms
        self.capacity = capacity


