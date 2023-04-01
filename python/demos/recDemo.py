class Rect(object):
  def __init__(self, width = 10, height = 20):
    self.width = width
    self.height = height
    
  def getWidth(self):
    return self.__width
  
  def getHeight(self):
    return self.__height
  
  def setWidth(self, width):
    self.__width = width
    
  def setHeight(self, height):
    self.__height = height
    
  def getPerimeter(self):
    return 2 * (self.width + self.height)
    
  def getArea(self):
    return self.width * self.height
  
  def getStats(self):
    output = """
width:     %d
height:    %d
area:      %d
perimeter: %d """ % (self.width, self.height,
                         self.area, self.perimeter)
    return output
  
  
  width = property(fget = getWidth, fset = setWidth)
  height = property(fget = getHeight, fset = setHeight)
  area = property(fget = getArea)
  perimeter = property (fget = getPerimeter)
  
def main():
  if __name__ == "__main__":
    a = Rect(5, 7)    
    print "area:      %d" % a.area
    print "perimeter: %d" % a.perimeter
    
    b = Rect()
    b.width = 10
    b.height = 20
    print b.getStats()
    
if __name__ == "__main__":
  main()
  