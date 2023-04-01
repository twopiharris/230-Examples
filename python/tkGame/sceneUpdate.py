""" spriteDemo.py
    building a sprite object
"""
from tkinter import *

class Sprite(object):
    def __init__(self, fileName, scene):
        object.__init__(self)
        self.__fileName = fileName
        self.__image = PhotoImage(file = fileName)
        self.__scene = scene
        self.__canvas = scene.canvas
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

    def start(self):
        """ begins the scene """
        self.hiddenUpdate()
        
    def hiddenUpdate(self):
        """ calls abstract update function,
            then calls itself
            This allows user to create update
            function without having to explicitly
            set the framerate behavior
            """
        self.update()
        after(50, self.hiddenUpdate)
        
    def update(self):
        """ abstract method - meant to be
            overwritten by developer """
        self.clear()
        self.mySprite.changeXby(5)
    
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Simple TK Game Engine")
        
        self.scene = Scene(self)
        
        self.scene.mySprite = Sprite("cowSmall.gif", self.scene)
        
        self.scene.start()
        self.mainloop()
    

def main():
    app = App()
    
if __name__ == "__main__":
    main()