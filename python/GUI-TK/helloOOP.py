""" helloOOP.py
    helloIO converted to OOP
"""

from Tkinter import *

class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    
    self.title("IO Demo")
    
    self.lblOutput = Label(self, text = "type your name")
    self.lblOutput.grid()
    
    self.txtInput = Entry(self)
    self.txtInput.grid()
    
    self.btnClickMe = Button(self, text = "Click Me", command = self.sayHi)
    self.btnClickMe.grid()
    
    self.mainloop()
    
  def sayHi(self):
    name = self.txtInput.get()
    self.lblOutput["text"] = "Hi there, %s" % name

def main():
  a = App()
  
if __name__ == "__main__":
  main()