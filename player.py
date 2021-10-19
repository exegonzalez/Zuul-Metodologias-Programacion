

class Player():

    def __init__(self, name, max_weight):
        self.name = name
        self.max_weight = max_weight
        self.items = {}
    
    def setItem(self, item):
        self.items[item.name] = item

    def print_items_information(self):
        print("Items: ")
        items = ''
        for item in self.items.keys():
            items += self.items[item].name + ' '
        print(items)