""" superCircle.py
    Extend circle from circleProperty
    Add area and circumference

"""

from circleProperty import *
import math

class SuperCircle(Circle):
  """ Improved circle with area and circumference """
  
  def __init__(self, radius):
    Circle.__init__(self, radius)
  
  def getCircumference(self):
    return self.radius * 2 * math.pi
  
  def getArea(self):
    return math.pi * (self.radius ** 2)

  #map methods to properties for convenience
  circumference = property(fget = getCircumference)
  area = property(fget = getArea)
  
def main():
  "test the SuperCircle"
  c = SuperCircle(50)
  print("radius:        {:.2f}".format(c.radius))
  print("circumference: {:.2f}".format(c.circumference))
  print("area:          {:.2f}".format(c.area))
  
if __name__ == "__main__":
  main()
