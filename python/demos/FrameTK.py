""" Hi user """

from Tkinter import *

class App(object):
  def __init__(self, master):
    self.frame = Frame(master)
    self.frame.grid()
    master.title("Hi there")
    
    self.lblOutput = Label(self.frame, text = "type your name")
    self.lblOutput.grid()
    
    self.txtInput = Entry(self.frame)
    self.txtInput.insert(INSERT, "anonymous")
    self.txtInput.grid()
    
    self.btnClickMe = Button(self.frame, text = "click me", command = self.clickMe)
    self.btnClickMe.grid()
    
  def clickMe(self):
    name = self.txtInput.get()
    self.lblOutput["text"] = "Hi there %s!" % name
    
def main():
  root = Tk()
  app = App(root)
  root.mainloop()
  
if __name__ == "__main__":
  main()
