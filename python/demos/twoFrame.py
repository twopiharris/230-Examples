"""
   twoFrame.py
"""
from Tkinter import *

class One(Tk):
  def __init__(self):
    Tk.__init__(self)
    self.title("form one")
    self.myLabel = Label(self, text = "Frame one")
    self.myLabel.grid()
    self.btnClose = Button(self, text= "close", command = self.destroy)
    self.btnClose.grid()
    self.mainloop()

class Two(Tk):
  def __init__(self):
    Tk.__init__(self)
    self.title("form two")
    self.myLabel = Label(self, text = "Frame two")
    self.myLabel.grid()
    self.btnClose = Button(self, text = "close", command = self.showResults)
    self.btnClose.grid()
    self.mainloop()
    
  def showResults(self):
    self.destroy()
    three = Three(5, 3)
    
class Three(Tk):
  def __init__(self, numQ, numCorrect):
    Tk.__init__(self)
    self.title("form three")
    self.myLabel = Label(self, text = str(numQ) + str(numCorrect))
    self.myLabel.grid()
    self.btnClose = Button(self, text = "close", command = self.destroy)
    self.btnClose.grid()
    self.mainloop()

def main():
  one = One()
  two = Two()

if __name__ == "__main__":
  main()
  