# keys.py
# work with the keyboard

from tkinter import *
from TKsimple import *

class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    
    self.scene = Scene(self, 600, 400)
    self.emu = Sprite("emuSmall.gif", self.scene, 50, 50)
    self.bg = Sprite("bg_1_1.gif", self.scene, 600, 400)
    
    self.bind("<Key>", self.checkKeys)
    
    #apparently you have to bind all the special keys!!
    self.bind("<Left>", lambda x: self.checkSpecial("left"))
    self.bind("<Right>", lambda x: self.checkSpecial("right"))
    self.bind("<Up>", lambda x: self.checkSpecial("up"))
    self.bind("<Down>", lambda x: self.checkSpecial("down"))
    self.bind("<space>", lambda x: self.checkSpecial("space"))
    
    self.bind("<KeyPress>", self.checkKeyPress)
    
    self.update()
    self.mainloop()
  
  def update(self):
    self.scene.refresh()    
    self.bg.refresh()
    self.emu.refresh()
    
    self.after(20, self.update)
  
  def checkKeys(self, event):
    print(event.char)
    
  def checkSpecial(self, key):
    if key == "left":
      self.emu.addForce(270, 2)
    if key == "right":
      self.emu.addForce(90, 2)
    if key == "up":
      self.emu.addForce(0, 2)
    if key == "down":
      self.emu.addForce(180, 2)
    if key == "space":
      self.emu.dx = 0
      self.emu.dy = 0
 
  def checkKeyPress(self, event):
    print("keycode: {} ".format(event.keycode))
    print("keysym: {} ".format(event.keysym))
    print("keysym_num: {} ".format(event.keysym_num))
    print("num: {} ".format(event.num))
  
    
def main():
  app = App()
  
if __name__ == "__main__":
  main()
