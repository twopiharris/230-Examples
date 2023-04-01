class Rectangle(object):
  def __init__(self, width = 5, height = 7):
    object.__init__(self)
    self.__width = width
    self.__height = height

  def setWidth(self, width):
    self.__width = width

  def setHeight(self, height):
    self.__height = height

  def getWidth(self):
    return self.__width

  def getHeight(self):
    return self.__height

  def getArea(self):
    return (self.width * self.height)

  width = property(fset = setWidth, fget = getWidth)
  height = property (fset = setHeight, fget = getHeight)
  area = property(fget = getArea)

def main():
    print ("Rectangle a:")
    a = Rectangle(5, 7)
    print "area:      %s" % a.area
    print a.getArea()

    #print ("perimeter: {}".format(a.perimeter))
    
    #print ("")
    #print ("Rectangle b:")
    b = Rectangle()
    b.width = 10
    b.height = 20
    #print (b.getStats())

if __name__ == "__main__":
  main()
