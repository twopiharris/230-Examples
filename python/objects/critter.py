""" Critter.py
    Basic critter class
    includes a constructor
"""
print "In critter.py, namespace is %s" % __name__
 
class Critter(object):
  def __init__(self):
    object.__init__(self)
    self.name = "Anonymous"
    
  def sayHi(self):
    print "Hi, my name is %s!" % self.name
    

def main():  
  c = Critter()
  c.name = "George"
  c.sayHi()
  
main()



