""" spriteDemo.py
    building a sprite object
"""
from tkinter import *

class Sprite(object):
    def __init__(self, fileName, scene, height, width):
        object.__init__(self)
        self.__fileName = fileName
        self.__image = PhotoImage(file = fileName)
        self.__scene = scene
        self.__canvas = scene.canvas
        self.__height = height
        self.__width = width
        self.__x = 100
        self.__y = 100    
    
    """ ----------------   X and Y ---------------- """    
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

    """ ---------------- Height and Width ---------------- """    

    def getHeight(self):
        return self.__height
    
    def setHeight(self, height):
        self.__height = height
        
    def getWidth(self):
        return self.__width
    
    def setWidth(self, width):
        self.__width = width
        
    height = property(fset = setHeight, fget = getHeight)
    width = property(fset = setWidth, fget = getWidth)
    
    """ ---------- Collision managment ---------- """
    def collidesWith(self, other):
        """ given another sprite, determines if this sprite
            and the other sprite are colliding """
        
        sLeft = self.x
        sRight = self.x + self.width
        sTop = self.y
        sBottom = self.y + self.height
        
        oLeft = other.x
        oRight = other.x + other.width
        oTop = other.y
        oBottom = other.y + other.height
        
        colliding = True
        if sRight < oLeft:
            colliding = False
        if sLeft > oRight:
            colliding = False
        if sTop > oBottom:
            colliding = False
        if sBottom < oTop:
            colliding = False
        
        return colliding
    
    
    def draw(self):
        """draws image to canvas"""
        self.__canvas.create_image(self.x,
                                 self.y,
                                 image = self.__image)

class Scene(object):
    def __init__(self, parent, width = 600, height = 400):
        object.__init__(self)
        self.__width = width
        self.__height = height
        self.__canvas = Canvas(parent,
                             height = self.height,
                             width = self.width,
                             bg = "white")
        self.__canvas.grid()
    
    def getWidth(self):
        return self.__width
    
    def setWidth(self, width):
        self.__width = width
    
    width = property(fget = getWidth, fset = setWidth)
    
    def getHeight(self):
        return self.__height
    
    def setHeight(self, height):
        self.__height = height
        
    height = property(fget = getHeight, fset = setHeight)
    
    def getCanvas(self):
        return self.__canvas
    
    canvas = property(fget = getCanvas)
    
    def clear(self):
        self.__canvas.create_rectangle(0, 0,
                                       self.width,
                                       self.height,
                                       fill = "white")

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Simple TK Game Engine")
        
        self.scene = Scene(self)
        
        self.mySprite = Sprite("cowSmall.gif", self.scene, 50, 50)
        self.otherSprite = Sprite("cowSmall.gif", self.scene, 50, 50)
        self.otherSprite.x = 200
        self.otherSprite.y = 100
        self.update()
        self.mainloop()
        
    def update(self):
        
        #clear background
        self.scene.clear()
        self.mySprite.changeXby(10)
        self.mySprite.draw()
        self.otherSprite.draw()
        if self.mySprite.collidesWith(self.otherSprite):
            print("collision")
        
        #repeat
        self.after(50, self.update)

def main():
    app = App()
    
if __name__ == "__main__":
    main()