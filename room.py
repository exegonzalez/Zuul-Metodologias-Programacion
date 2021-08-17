
class Room:
    def __init__(self, description):
        self.description = description
        self.northExit = None
        self.southExit = None
        self.eastExit = None
        self.westExit = None

    def setExits(self, north, east, south, west):
        if(north != None):
            self.northExit = north
        if(east != None):
            self.eastExit = east
        if(south != None):
            self.southExit = south
        if(west != None):
            self.westExit = west
        return

    def getDescription(self):
        return self.description
