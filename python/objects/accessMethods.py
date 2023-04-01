""" accessMethods.py
    demonstrates getters and setters
"""

class Critter(object):
  def __init__(self, name = "Anonymous"):
    self.name = name
    
  def getName(self):
    return self.name
    
  def setName(self, name):
    self.name = name
    
if __name__ == "__main__":    
  c = Critter()
  c.setName("Marge")
  print c.getName()

