""" clone.py
    illustrates default inheritance
"""

from critterModule import *

class Clone(Critter):
  def __init__(self):
    Critter.__init__(self)
    
def main():
  c = Clone()
  #clone automatically has properties and methods of
  #parent class
  c.name = "Martha"
  c.sayHi()
  
if __name__ == "__main__":
  main()
  
  
  
  
  