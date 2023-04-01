""" spriteDemo.py
    building a sprite object
"""
from tkinter import *
import random
from TKSimple import *
import math

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("TKSimple Demo")
        
        self.scene = Scene(self, 750, 600)
        self.background = Sprite("bg_1_1.gif", self.scene, 800,1100)
        self.emu = Sprite("emuSmall.gif", self.scene, 50, 50)
        self.cow = Sprite("cowSmall.gif", self.scene, 50, 50)

        self.cow.x = 375
        self.cow.y = 300

        self.emu.boundAction = "BOUNCE"

        self.bind("<KeyPress>", self.keyDown)

        self.refresh()
        self.mainloop()

    def refresh(self):
        
        self.scene.clear()
        self.scene.refresh()
        self.background.refresh()
        self.emu.refresh()
        self.cow.refresh()

        self.emu.addForce(self.emu.angleTo(self.cow), .5)

        if (self.emu.collidesWith(self.cow)):
            print("KAPOW COW!!!")
            
        self.after(50, self.refresh)
    
    def keyDown(self, event):
        if event.char == "a":
            self.emu.addForce(270, 2)
        if event.char == "d":
            self.emu.addForce(90, 2)
        if event.char == "w":
            self.emu.addForce(0, 2)
        if event.char == "s":
            self.emu.addForce(180, 2)



def main():
   app = App() 
    
if __name__ == "__main__":
    main()
