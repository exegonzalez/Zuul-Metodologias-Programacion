

class Item:

    def __init__(self, name, description, weight, picked_up=True):
        self.name = name
        self.description = description
        self.weight = weight
        self.picked_up = picked_up


class Comestible(Item):
    
    def __init__(self, name, description, weight, incremet, atribute, picked_up=True):
        super().__init__(name, description, weight, picked_up)
        self.increment = incremet
        self.atribute = atribute
    
    def comer(self, player):
        print('se come el item')
        player.fuera += self.increment
