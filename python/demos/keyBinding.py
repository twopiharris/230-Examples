""" keyboard binding demo """

from Tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.lblOutput = Label(self, text = "press a key")
        self.lblOutput.grid()
        self.bind("<Key>", self.checkKeys)
        
        self.mainloop()
        
    def checkKeys(self, event):
        self.lblOutput["text"] = "You pressed %s." % event.keysym

def main():
    app = App()
    
if __name__ == "__main__":
    main()
    
    
