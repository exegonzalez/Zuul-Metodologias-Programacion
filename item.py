

class Item:

    def __init__(self, name, description, weight, picked_up=True, comestible=False):
        self.name = name
        self.description = description
        self.weight = weight
        self.picked_up = picked_up
        self.comestible = comestible
