""" basic digital clock in python 
    illustrates after to build 
    a timing loop for animation
    and whatever other purpose """

from Tkinter import *
import time

class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    self.lblTimer = Label(text = "timer")
    self.lblTimer.grid()
    self.updateClock()
    
    self.mainloop()

  def updateClock(self):
    currentTime = time.strftime("%H: %M: %S")
    self.lblTimer["text"] = currentTime
    self.after(500, self.updateClock)

def main():
  a = App()

if __name__ == "__main__":
  main()
