""" properties.py
    illustrates using properties
    to automate access methods
    also illustrtes 'hidden' data fields
"""

class Critter(object):
  def __init__(self, name = "Anonymous"):
    object.__init__(self)
    # the next line only makes sense when you understand
    # the property defined below
    self.name = name
    
  def getName(self):
    return self.__name
  
  def getFormalName(self):
    #getters can be derived data
    return self.__name + ", Destroyer of Worlds"
  
  def setName(self, name):
    #access methods can be filtered
    if len(name) < 5:
      print "name is too short"
      name = "Anonymous"
    self.__name = name
    
  name = property(fget = getFormalName, fset = setName)
    
def main():
  c = Critter("George")
  
  # this won't work, because __name is hidden
  #print c.__name
  
  # the access methods work as expected
  print c.getName()
  c.setName("Froofie")
  print c.getName()
  
  # since the property is defined, the name attribute
  # 'feels' like a real attribute, but it quietly
  # works through the modifiers
  
  c.name = "Joy"
  print c.name
  
if __name__ == "__main__":
  main()
  