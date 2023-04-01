""" method.py
    add a method to the basic
    critter object
"""

class Critter(object):
  name = "Anonymous"
  def sayHi(self):
    print("Hi, my name is {}".format(self.name))
    
c = Critter()
c.name = "Martha"
c.sayHi()
