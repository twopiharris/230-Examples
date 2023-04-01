""" spriteDemo.py
    building a sprite object
"""
from tkinter import *

class Sprite(object):
    def __init__(self, fileName, canvas):
        self.__fileName = fileName
        self.__image = PhotoImage(file = fileName)
        self.__canvas = canvas
        self.__x = 100
        self.__y = 100
        
    def setX(self, x):
        self.__x = x
    
    def getX(self):
        return(self.__x)
    
    def setY(self, y):
        self.__y = y
    
    def getY(self):
        return(self.__y)
    
    def changeXby(self, dx):
        self.x += dx
        #wrap
        if self.x > 600:
            self.x = 0
        if self.x < 0:
            self.x = 600
    
    def changeYby(self, dy):
        self.y += dy
        if self.y > 400:
            self.y = 0
        if self.y < 0:
            self.y = 400
    
    x = property(fset = setX, fget = getX)
    y = property(fset = setY, fget = getY)

    def draw(self):
        """draws image to canvas"""
        self.__canvas.create_image(self.x,
                                 self.y,
                                 image = self.__image)



class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Basic animation loop")
        self.HEIGHT = 400
        self.WIDTH = 600
        
        self.canvas = Canvas(self, height = self.HEIGHT,
                             width = self.WIDTH, bg = "white")
        self.canvas.grid()
        
        self.mySprite = Sprite("cowSmall.gif", self.canvas)
        
        self.update()
        self.mainloop()
        
    def clear(self):
        #clear canvas
        self.canvas.create_rectangle(0, 0, self.WIDTH,
                                     self.HEIGHT, fill = "white")
        
    def update(self):
        
        #clear background
        self.clear()
        self.mySprite.changeXby(10)
        self.mySprite.draw()

        #repeat
        self.after(50, self.update)

def main():
    app = App()
    
if __name__ == "__main__":
    main()