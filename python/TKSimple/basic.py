# basic.py
# simplest possible example

from tkinter import *
from TKSimple import *

class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    
    self.title("basic TKGame demo")
    #make the scene
    #parameters are TK object, width, height
    self.scene = Scene(self, 600, 400)
    
    #make a sprite
    #parameters are image (must be gif), scene, width, height
    self.emu = Sprite("emuSmall.gif", self.scene, 50, 50)
    
    #move three pixels to right every frame
    self.emu.dx = 3
    
    #start the main loop
    self.update()
    self.mainloop()
    
  def update(self):
    self.scene.refresh()
    self.emu.refresh()
    
    #run this function again after 50ms (20fps)
    self.after(50, self.update)
    
def main():
  app = App()
  
if __name__ == "__main__":
  main()
