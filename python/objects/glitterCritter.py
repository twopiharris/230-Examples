""" glitterCritter.py
    demonstrates inheritance
    
"""

from critterModule import *

class GlitterCritter(Critter):
  def __init__(self):
    Critter.__init__(self)
    
  def sayHi(self):
    #overwrite the sayHi method to do something new
    print "%s gently shimmers" % self.name

def main():
  g = GlitterCritter()
  g.name = "George"
  g.sayHi()
  
  

if __name__ == "__main__":
  main()
  
