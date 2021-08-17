
class Command:
    
    def __init__(self, firstWord=None, secondWord=None):
        self.commandWord = firstWord
        self.secondWord = secondWord

    def getCommandWord(self):
        return self.commandWord

    def getSecondWord(self):
        return self.secondWord
    
    def isUnknown(self):
        return (self.commandWord is None)

    def hasSecondWord(self):
        return (self.secondWord is not None)