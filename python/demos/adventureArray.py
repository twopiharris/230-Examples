class Node(object):
    def __init__(self, name, description, aMenu, a, bMenu, b):
        object.__init__(self)
        self.name = name
        self.description = description
        self.aMenu = aMenu
        self.a = a
        self.bMenu = bMenu
        self.b = b

    def toString(self):
        output = self.name + "\n"
        output += self.description + "\n"
        output += "a) %s (%d) \n" % (self.aMenu, self.a)
        output += "b) %s (%d) \n" % (self.bMenu, self.b)
        return output;
        
    def process(self):
        
        #prints out a menu and returns a new node
        print self.description
        print "A) %s" % self.aMenu
        print "B) %s" % self.bMenu
    
        response = raw_input("what do you want to do? ")
        if response == "a":
            nextNode = self.a
        elif response == "b":
            nextNode = self.b
        else:
            print "That is not a valid answer"
            print "Starting over..."
            nextNode = 0
        print
        return nextNode 
        
        
game = []

def main():
    #pdb.set_trace()
    game.append(Node("Start", "You're on a boat. It's on fire",
                     "Stay on the ship", 1,
                     "Jump in the water" ,2))
    game.append(Node("You're on the ship", "It's ON FIRE!!! You die",
                     "Start over", 0,
                     "Quit", 3))
    game.append(Node("in the water", "You win!",
                     "start over", 0,
                     "quit", 3))
    game.append(Node("quit", "You quit",
                     "game over", 0,
                     "game over", 0))
    
    location = 0
    QUITLOC = 3
    while (location != QUITLOC):
        curNode = game[location]
        location = curNode.process()
        #location = processNode(location)

if __name__ == "__main__":
    main()
