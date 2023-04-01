""" frameDemo.py 
    illustrates swapping out frames
    for a more complex ui
"""
from Tkinter import *


class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    
    self.frmMain = Frame(self)
    #attach this element to the main object
    self.frmMain.grid(row = 0, column = 0, rowspan = 4, columnspan = 2)
    #attach labels or other widgets to frame, not to main
    Label(self.frmMain, text = "main frame").grid()
    Label(self.frmMain, text = "main frame").grid()
    Label(self.frmMain, text = "main frame").grid()
    Label(self.frmMain, text = "main frame").grid()

    #alternate panel not currently displayed
    self.frmAlt = Frame(self)
    Label(self.frmAlt, text = "alternate frame").grid()
    Label(self.frmAlt, text = "alternate frame").grid()
    Label(self.frmAlt, text = "alternate frame").grid()
    Label(self.frmAlt, text = "alternate frame").grid()

    self.btnMain = Button(self, text = "main", command = self.showMain)
    self.btnMain.grid(row = 4, column = 0)

    self.btnAlt = Button(self, text = "alt", command = self.showAlt)
    self.btnAlt.grid(row = 4, column = 1)

    self.mainloop()

  def showMain(self):
    #grid_forget removes element from grid layout, but 
    #keeps it in memory (destroy() eliminates it altogether)
    #remove other layout from grid
    self.frmAlt.grid_forget()
    #add this layout to grid
    self.frmMain.grid(row = 0, column = 0, rowspan = 4, columnspan = 2)

  def showAlt(self):
    self.frmMain.grid_forget()
    self.frmAlt.grid(row = 0, column = 0, rowspan = 4, columnspan = 2)

def main():
  a = App()

if __name__ == "__main__":
  main()

