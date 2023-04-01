""" circle.py
    illustrates why data hiding
    is a good idea
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
      self.radius = 10
    elif (radius > 100):
      print("Radius must be 100 or less")
      print("Setting radius to 10")
      self.radius = 10
    else:
      self.radius = radius

  def getRadius(self):
    return self.radius
  
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
  print(c.getDiameter())
  c.setDiameter(60)
  print(c.getRadius())
  
  # PROBLEM:  It's still possible to directly set radius to an illegal value:
  c.radius = -50
  print(c.getDiameter())
  
if __name__ == "__main__":
  main()
  
