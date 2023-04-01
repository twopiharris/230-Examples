from tkinter import *
import random
import math

#import msvcrt Windows only library - not used so removed (sound effects?)

class Sprite(object):
    """ A sprite object for the TK canvas
        
        INITIALIZATION
        filename:   the address of the image file
                    (default is in same directory as code)
        
        scene:      the scene to which the sprite belongs
        
        height:
        width:      height and width of the
                    actual image file.  (you cannot CHANGE height
                    and widht here.  We'll use scale for that later)
       
        Sprite has basic motion and collision behavior.
        
        PROPERTIES:
        x, y:           x and y position of the upper-left
                        corner of the sprite
        
        height, width: size of sprite's COLLISION box
                       doesn't effect visual size of image
                       
        boundAction: This sets what action the sprite will take
                      when the sprite goes off the borders of the scene.
                      The following options are valid:
                      WRAP: (default) This causes the sprite to appear on
                      the opposite side of the screen,
                      CONTINUE: The sprite continues in its direction, going
                      off-screen, but it still exists.
                      BOUNCE: The sprite reflects off of the side of the scene.
                      KILL: The sprite is set to visible = false.
                      CUSTOM: The sprite calls the customBoundAction() method.
                      This method exists to be overwritten. When it is called,
                      the side that the sprite leaves the scene through is passed
                      to the method (UP, DOWN, LEFT, RIGHT).

        
                       
        METHODS
        
        changeXby(changeX): change x by dx pixels immediately
        changeYby(changeY): change y by dy pixels immediately

        changeDXby(changeDX): change dx by changeDX per frame pixels immediately
        changeDYby(changeDY): change dy by changeDY per frame pixels immediately

        angleTo(sprite): returns the angle in degrees to the indicated sprite
        
        addForce(angle, speed): This adds a vector force to the sprite at the
                                given angle and at the given speed (in pixels
                                per frame).
        
        
        collidesWith(sprite):
                        Given another sprite, returns True
                        if this sprite and the other sprite
                        are currently colliding.  Standard
                        rectangular bounding box collision
        
        draw():         draws the sprite at the current
                        (x, y) position on the screen.
                        Should be called once per frame.
    """

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
        self.__dx = 0
        self.__dy = 0
        self.__visible = True
        self.__boundAction = "WRAP"
        
        
    
    """ ----------------   X and Y ---------------- """    
    def setX(self, x):
        self.__x = x
    
    def getX(self):
        return(self.__x)
    
    def setY(self, y):
        self.__y = y
    
    def getY(self):
        return(self.__y)

    def getDX(self):
        return(self.__dx)

    def getDY(self):
        return(self.__dy)

    def setDX(self, dx):
        self.__dx = dx

    def setDY(self, dy):
        self.__dy = dy

    def setBoundAction(self, action):
        if action in ("WRAP", "CONTINUE", "BOUNCE", "KILL", "CUSTOM"):
            self.__boundAction = action
        else:
            print("'"+action+"' is not a valid bound action.")
            print("If you want to make your own, overwrite customBound() and")
            print("set the boundAction to CUSTOM.")
            
    def getBoundAction(self):
        return self.__boundAction
        
    def changeXby(self, changeX):
        self.x += changeX
        
        
    
    def changeYby(self, changeY):
        self.y += changeY

    def changeDXby(self, changeDX):
        self.dx += changeDX

    def changeDYby(self, changeDY):
        self.dy += changeDY

    
    def angleToRad(self, degrees):
        
        radians = ((degrees - 90) * math.pi) / 180
        return radians

    def angleTo(self, otherSprite):
        diffX = otherSprite.x - self.x
        diffY = (otherSprite.y - self.y)
        radAngle = math.atan2(diffY, diffX)
        degrees = radAngle * 180 / (math.pi)
        
        degrees += 90
        return degrees
    
    
    def addForce(self, angle, speed):
        angle = self.angleToRad(angle)
        self.__dx += speed * math.cos(angle)
        self.__dy += speed * math.sin(angle)
        
    
    x = property(fset = setX, fget = getX)
    y = property(fset = setY, fget = getY)
    dx = property(fset = setDX, fget = getDX)
    dy = property(fset = setDY, fget = getDY)
    boundAction = property(fset = setBoundAction, fget = getBoundAction)
    

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
        if self.__visible:
            self.__canvas.create_image(self.x,
                                     self.y,
                                     image = self.__image)

    def refresh(self):
        """ Calling refresh() for any Sprite does the following:
         1) Runs update()
         2) Adjusts the position of the Sprite by dx and dy.
         3) Checks bounds according to the set bound action (see: boundAction)
         4) If the Sprite's visible attribute is set to True, it draws the Sprite.

         The update() method is intended to be overwritten if needed. If it is not,
         it changes the Sprite's x and y values by dx and dy, respectively. Remember
          that if you overwrite update(), you must account for this."""
        
        self.update()
        self.x += self.dx
        self.y += self.dy
        self.checkBounds()
        if (self.__visible):
            
            self.draw()

    def checkBounds(self):
        goneLeft = False
        goneRight = False
        goneUp = False
        goneDown = False
        
        #see if we are off the sides
        if self.__x < 0:
            goneLeft = True
        if self.__y < 0:
            goneUp = True
        if self.__y > self.__scene.height:
            goneDown = True
        if self.__x > self.__scene.width:
            goneRight = True

        #behavior appropriate to bound action

        if (self.boundAction == "WRAP"):
            if (goneLeft):
                self.__x = self.__scene.width
            elif (goneRight):
                self.__x = 0
            elif (goneUp):
                self.__y = self.__scene.height
            elif (goneDown):
                self.__y = 0
        elif (self.boundAction == "BOUNCE"):
            if (goneLeft):
                self.__x = 0
                self.__dx = self.__dx * -1
            if (goneRight):
                self.__x = self.__scene.width
                self.__dx = self.__dx * -1
            if (goneUp):
                self.__y = 0
                self.__dy = self.__dy * -1
            if (goneDown):
                self.__y = self.__scene.height
                self.__dy = self.__dy * -1
        elif (self.boundAction == "KILL"):
            if (goneLeft or goneRight or goneUp or goneDown):
                self.__visible = False
                self.__dx = 0
                self.__dy = 0
        elif (self.boundAction == "CUSTOM"):
            if (goneLeft):
                customBoundAction("LEFT")
            if (goneRight):
                customBoundAction("RIGHT")
            if (goneUp):
                customBoundAction("UP")
            if (goneDown):
                customBoundAction("DOWN")
        
        
    def update(self):
        """ intended to be overwritten"""
        pass
        
    def customBoundAction(self, direction):
        """ intended to be overwritten"""
        pass

class Scene(object):
    """ Basic Scene object for Tk
        Encapsulates canvas element.
        
        INITIALIZATION
        parent:     Tk document this scene will be added to
                    Automatically creates a canvas element
                    and uses the grid layout (with no paramters)
                    to add the component to the TK object.
                    
        width:      Width of the Tk grid element in pixels
        height:     Height of the Tk grid element in pixels
    
        PROPERTIES
        width:
        height:
        canvas:
        currentKey:  (read-only)

        METHODS
        clear:
        
        update:    Intended to be overwritten
    """
        
    def __init__(self, parent, width = 600, height = 400):
        object.__init__(self)
        self.__width = width
        self.__height = height
        self.__parent = parent
        self.__currentKey = ""
        self.__canvas = Canvas(parent,
                             height = self.height,
                             width = self.width,
                             bg = "white")
        self.__canvas.grid()        
        self.initKeys()
        
    
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
        self.__canvas.delete("all")
        self.__canvas.create_rectangle(0, 0,
                                       self.width,
                                       self.height,
                                       fill = "white")

    def update(self):
        """This is intended to be overwritten"""
        pass
    
    def refresh(self):
        #clear the display image
        self.clear()
        
        #call anything in my update
        self.update()
        
        #clear the current key buffer
        self.__currentKey = ''

    def angleToRad(self, degrees):
        
        radians = math.radians(degrees - 90)
        return radians    
        
    def start(self):
        pass

    def getCurrentKey(self):
      return self.__currentKey

    currentKey = property(fget = getCurrentKey)

    def initKeys(self):

        print("I got to initKeys")

        #initializes keyboard input

        #bind standard keys to checkKeys method
        self.__parent.bind("<Key>", self.checkKeys)

        #bind special keys individually
        self.__parent.bind("<Left>", lambda x: self.checkSpecial("left"))
        self.__parent.bind("<Right>", lambda x: self.checkSpecial("right"))
        self.__parent.bind("<Up>", lambda x: self.checkSpecial("up"))
        self.__parent.bind("<Down>", lambda x: self.checkSpecial("down"))
        self.__parent.bind("<space>", lambda x: self.checkSpecial("space"))
 
        #keypress not used yet
        #hope to bypass keyboard buffer
        #self.__parent.bind("<KeyPress>", self.checkKeyPress)

    def checkSpecial(self, key):
        self.__currentKey = key

    def checkKeys(self, event):
        self.__currentKey = event.char 

    def checkKeyPress(self, event):
        self.__currentKey = event.char
