""" circlePrivate.py
    hides radius so only access
    is through modifiers
    note that self.radius is changed to
    self.__radius throughout
"""

class Circle(object):
  def __init__(self, radius = 10):
    object.__init__(self)
    self.setRadius(radius)
    
  def setRadius(self, radius):
    #radius must be larger than 0 and less than or equal to 100
    if (radius <= 0):
      print "Radius must be larger than 0."
      print "Setting radius to 10."
      self.__radius = 10
    elif (radius > 100):
      print "Radius must be 100 or less"
      print "Setting radius to 10"
      self.__radius = 10
    else:
      self.__radius = radius

  def getRadius(self):
    return self.__radius
  
  def setDiameter(self, diameter):
    # Diameter doesn't really exist
    # If the user sets the diameter, that should
    # really set the radius
    self.setRadius(diameter / 2.0)
  
  def getDiameter(self):
    # Diameter doesn't really exist.
    # It is dependent on radius, so calculate it
    return 2 * self.getRadius()
  
def main():
  c = Circle(50)
  c.setRadius(150)
  print c.getDiameter()
  c.setDiameter(60)
  print c.getRadius()
  
  #now attempting to modify c.radius directly will have no effect

if __name__ == "__main__":
  main()
  