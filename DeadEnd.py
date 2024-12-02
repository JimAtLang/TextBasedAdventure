from Passage import Passage

class DeadEnd(Passage):
    def __init__(self, name, desc, from_room, from_dir):
        super().__init__(self, name, desc, from_room, from_dir, None)
