from room import Room
from item import Item
from player import Player
from stack import Stack, inverse
from parser import Parser


class Game:
    def __init__(self):
        self.createRooms()
        self.player = Player('jugador 1', 20)
        self.parser = Parser()
        self.stack = Stack()

    def createRooms(self):
        outside = Room("outside the main entrance of the university")
        theater = Room("in a lecture theater")
        pub = Room("in the campus pub")
        lab = Room("in a computing lab")
        office = Room("in the computing admin office")
        basement = Room("in the basement")
        patio = Room("in the patio")

        outside.setExits(None, theater, lab, pub, None, None, patio)
        theater.setExits(None, None, None, outside, None, basement, None)
        pub.setExits(None, outside, None, None, None, None, None)
        lab.setExits(outside, office, None, None, None, None, None)
        office.setExits(None, None, None, lab, None, None, None)
        basement.setExits(None, None, None, None, theater, None, None)

        espada = Item('espada', 'esto es una espada oxidada', 19)
        zapatillas = Item('zapatilla', 'esto es un par de zapatillas viejas..', 2.87)
        silla = Item('silla', 'una silla para descansar', 2)
        ropero = Item('ropero', 'una ropero antiguo', 15, picked_up=False)
        outside.setItem(espada)
        outside.setItem(zapatillas)
        outside.setItem(ropero)
        theater.setItem(silla)

        self.currentRoom = outside

        return

    def play(self):
        self.printWelcome()

        finished = False
        while(not finished):
            command = self.parser.getCommand()
            finished = self.processCommand(command)
        print("Thank you for playing.  Good bye.")

    def printWelcome(self):
        print()
        print("Welcome to the World of Zuul!")
        print("World of Zuul is a new, incredibly boring adventure game.")
        print("Type 'help' if you need help.")
        print("")
        self.currentRoom.print_location_information()
        print()

    def processCommand(self, command):
        wantToQuit = False

        if(command.isUnknown()):
            print("I don't know what you mean...")
            return False

        commandWord = command.getCommandWord()
        if(commandWord == "help"):
            self.printHelp()
        elif(commandWord == "go"):
            self.goRoom(command)
        elif(commandWord == "quit"):
            wantToQuit = self.quit(command)
        elif(commandWord == "look"):
            self.look_items()
        elif(commandWord == "bag"):
            self.bag_items()
        elif(commandWord == "back"):
            self.goBack()
        elif(commandWord == "take"):
            self.takeItem(command)

        return wantToQuit

    def printHelp(self):
        print("You are lost. You are alone. You wander")
        print("around at the university.")
        print()
        print("Your command words are:")
        print("   go quit help")

    def goRoom(self, command):
        if(not command.hasSecondWord()):
            print("Go where?")
            return

        direction = command.getSecondWord()
        nextRoom = self.currentRoom.get_exit(direction)
       
        if(nextRoom is None):
            print("There is no door!")
        else:
            self.currentRoom = nextRoom
            self.currentRoom.print_location_information()
            self.stack.push(direction)
            print()
    
    def takeItem(self, command):
        if(not command.hasSecondWord()):
            print("Take what?")
            return

        item_name = command.getSecondWord()
        item = self.currentRoom.getItem(item_name)
       
        if(item is None):
            print("There is not item in the room with this name!")
        else:
            if(item.picked_up):
                if(self.player.can_picked_up_new_item(item.weight)):
                    self.player.setItem(item)
                else:
                    print('no puedes levantar tanto peso...')
                    self.currentRoom.setItem(item)
            else:
                print('ese item no puede ser levantado')
                self.currentRoom.setItem(item)


    def look_items(self):
        self.currentRoom.print_items_information()

    def bag_items(self):
        self.player.print_items_information()
    
    def goBack(self):
        direction = self.stack.pop()
        if(direction):
            nextRoom = self.currentRoom.get_exit(direction)
       
            if(nextRoom is None):
                print("There is no door! to go", direction)
                self.stack.push(inverse[direction])
            else:
                self.currentRoom = nextRoom
                self.currentRoom.print_location_information()
                print()
        else:
            print('you are in the initial position, can not go back')

    def quit(self, command):
        if(command.hasSecondWord()):
            print("Quit what?")
            return False
        else:
            return True

g = Game()
g.play() 