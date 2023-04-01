""" adventureGUI.py """
from Tkinter import *

class Node(object):
    def __init__(self, name, description, aMenu, a, bMenu, b):
        object.__init__(self)
        self.name = name
        self.description = description
        self.aMenu = aMenu
        self.a = a
        self.bMenu = bMenu
        self.b = b

class Game(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("adventure game")

        self.currentNodeID = 0
        self.QUITLOC = 3

        self.setUpGame()

        #set up GUI
        self.lblDescription = Label(self, text = "description")
        self.lblDescription.grid(row = 0, columnspan = 2)

        self.btnA = Button(self, text = "A",
                           width = 20,
                           command = self.processA)
        self.btnA.grid(row = 1, column = 0)

        self.btnB = Button(self, text = "B",
                           width = 20,
                           command = self.processB)
        self.btnB.grid(row = 1, column = 1)

        self.display()
        self.mainloop()

    def processA(self):
        currentNode = self.story[self.currentNodeID]
        next = currentNode.a
        if next == self.QUITLOC:
            self.destroy()
        else:
            self.currentNodeID = next
            self.display()

    def processB(self):
        currentNode = self.story[self.currentNodeID]
        next = currentNode.b
        if next == self.QUITLOC:
            self.destroy()
        else:
            self.currentNodeID = next
            self.display()

    def setUpGame(self):
        self.story = []
        """sets up the node array"""
        self.story.append(Node("Start", "You're on a boat. It's on fire",
                               "Stay on the ship", 1,
                               "Jump in the water" ,2))
        self.story.append(Node("You're on the ship", "It's ON FIRE!!! You die",
                               "Start over", 0,
                               "Quit", 3))
        self.story.append(Node("in the water", "You win!",
                               "start over", 0,
                               "quit", 3))
        self.story.append(Node("quit", "You quit",
                               "game over", 0,
                               "game over", 0))

    def display(self):
        """ displays the current node """
        currentNode = self.story[self.currentNodeID]
        self.lblDescription["text"] = currentNode.description
        self.btnA["text"] = currentNode.aMenu
        self.btnB["text"] = currentNode.bMenu

def main():
    game = Game()

if __name__ == "__main__":
    main()
