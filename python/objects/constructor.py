"""constructor.py
   illustrate instance variables and constructor
"""

class Critter(object):
  #name is an instance variable
  name = "Anonymous"

  #constructor is called when new critter is created
  def __init__(self):
    #begin by initializing parent class
    object.__init__(self)
    
    #constructors usually initialize instance variables
    self.name = "Anonymous"
    
def main():
  c = Critter()
  print c.name
  c.name = "George"
  print c.name

if __name__ == "__main__":
  main()