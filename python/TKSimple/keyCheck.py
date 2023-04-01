#keyCheck.py
#basic example with keyboard input

from tkinter import *
from TKSimple import *

class App(Tk):
  def __init__(self):
    Tk.__init__(self)

    self.title("TKsimple with keyboard")

    self.scene = Scene(self, 600, 400)

    self.emu = Sprite("emuSmall.gif", self.scene, 50, 50)

    self.update()
    self.mainloop()

  def update(self):

    if self.scene.currentKey == 'left':
      self.emu.x -= 5
    elif self.scene.currentKey == 'right':
      self.emu.x += 5
    elif self.scene.currentKey == 'w':
      self.emu.y -= 5
    elif self.scene.currentKey == 's':
      self.emu.y += 5
      
    self.scene.refresh()
    self.emu.refresh()

    self.after(50, self.update)

def main():
  app = App()

if __name__ == "__main__":
  main()


