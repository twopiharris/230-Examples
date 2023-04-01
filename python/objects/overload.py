""" overload.py
    overloaded methods
    (particularly constructor)
"""

class Critter(object):
    
  def __init__(self, name = "Anonymous"):
    object.__init__(self)
    self.name = name
    
  def sayHi(self):
    print "Hi, may name is %s!" % self.name
    
c = Critter()
c.sayHi()
d = Critter("George")
d.sayHi()
