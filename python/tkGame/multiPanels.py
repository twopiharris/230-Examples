""" multiPanels.py
    illustrating multiple panels in Tkinter
"""

from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.state = "A"
        self.lblA = Label(self, text = "Hi there. A.", width = 30)
        self.lblA.grid(row = 0, column = 0)
                
        self.ctrB = FrmCount(self)
        #build but don't add to GUI
        #self.counter.grid()
        
        self.btnSwitch = Button(self, text = "switch", command = self.switch)
        self.btnSwitch.grid()
        
        self.mainloop()
        
    def switch(self):
        if self.state == "A":
            self.state = "B"
            self.lblA.grid_remove()
            self.ctrB.grid(row = 0, column = 0)
        else:
            self.state = "A"
            self.ctrB.grid_remove()
            self.lblA.grid(row = 0, column = 0)

class FrmCount(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.lblOut = Label(self, text = "click a button", width = 30)
        self.lblOut.grid()
        
        self.btnOne = Button(self, text = "One", command = self.sayOne)
        self.btnOne.grid(sticky = "we")
        
        self.btnTwo = Button(self, text = "Two",  command = self.sayTwo)
        self.btnTwo.grid(sticky = "we")
        
        self.btnThree = Button(self, text = "Three", command = self.sayThree)
        self.btnThree.grid(sticky = "we")
        
        
        
    def sayOne(self):
        self.lblOut["text"] = "uno"
        
    def sayTwo(self):
        self.lblOut["text"] = "dos"
        
    def sayThree(self):
        self.lblOut["text"] = "tres"

def main():
    app = App()
    
if __name__ == "__main__":
    main()

