from Actions import Actions

class GameObject:
    def __init__(self, name, desc, contains = None, flags = None, synonyms = None, capacity = 0):
        self.name = name
        self.desc = desc
        self.flags = flags
        if not contains:
            contains = []
        else:
            contains = contains
        self.actions = {}
        self.synonyms = synonyms
        self.capacity = capacity


