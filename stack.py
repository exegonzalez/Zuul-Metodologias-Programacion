
inverse = {'north': 'south',
           'south': 'north',
           'west': 'east',
           'east': 'west',
           'up': 'down',
           'down': 'up',
           'window': 'window',
           }

class Stack():

    def __init__(self):
        self.steps = []
    
    def push(self, data):
        if(data in inverse):
            self.steps.append(inverse[data])
    
    def pop(self):
        if(self.steps):
            return self.steps.pop()
        else:
            return None
