""" circleProperty.py
    create new 'virtual properties'
    so user thinks radius and diameter are actual properties
    but route access through modifiers
"""

class Circle(object):
  def __init__(self, radius = 10):
    object.__init__(self)
    self.setRadius(radius)
    
  def setRadius(self, radius):
    #radius must be larger than 0 and less than or equal to 100
    if (radius <= 0):
      print("Radius must be larger than 0.")
      print("Setting radius to 10.")
      self.__radius = 10
    elif (radius > 100):
      print("Radius must be 100 or less")
      print("Setting radius to 10")
      self.__radius = 10
    else:
      self.__radius = radius

  def getRadius(self):
    return self.__radius
  
  radius = property(fget = getRadius, fset = setRadius)
  
  def setDiameter(self, diameter):
    # Diameter doesn't really exist
    # If the user sets the diameter, that should
    # really set the radius
    self.setRadius(diameter / 2.0)
  
  def getDiameter(self):
    # Diameter doesn't really exist.
    # It is dependent on radius, so calculate it
    return 2 * self.getRadius()
  
  diameter = property(fget = getDiameter, fset = setDiameter)
  
def main():
  c = Circle(50)
  # now I can treat radius and diameter like properties
  # and the appropriate access methods will automatically be
  # invoked
  
  c.radius = -5
  print(c.diameter)
  c.diameter = 50
  print(c.radius)
  
if __name__ == "__main__":
  main()
  
