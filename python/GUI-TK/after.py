""" after demo
    illustrates the tk after function
"""
from Tkinter import *

class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    
    Label(self, text = "count:", anchor = "e").grid(row = 0, column = 0)
    self.lblOutput = Label(self, text = "0")
    self.lblOutput.grid(row = 0, column = 1 )
    
    self.title("automatic counter")
    self.after(10, self.update)
    self.mainloop()
    
  def update(self):
    counter = int(self.lblOutput["text"])
    counter += 1
    self.lblOutput["text"] = counter
    self.after(10, self.update)
    
def main():
  app = App()
  
if __name__ == "__main__":
  main()