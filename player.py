

class Player():

    def __init__(self, name, max_weight):
        self.name = name
        self.max_weight = max_weight
        self.items = {}
        self.strength = 1
        self.defese = 1
        self.equipment = {'casco': None, 'arma': None, 'armadura': None}
    
    def setItem(self, item):
        self.items[item.name] = item

    def print_items_information(self):
        print("Items: ")
        items = ''
        for item in self.items.keys():
            items += self.items[item].name + ' '
        print(items)
        print('peso total')

    def can_picked_up_new_item(self, weight):
        peso_total = 0
        for item in self.items.values():
            peso_total += item.weight
        peso_total += weight
        return peso_total <= self.max_weight

    def getItem(self, item):
        if(item in self.items):
            return self.items.pop(item)
        else:
            return None
