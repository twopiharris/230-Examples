""" CritterModule.py
    Basic critter class """
    
class Critter(object):
  def __init__(self):
    object.__init__(self)
    self.name = "I have no name"
    
  def sayHi(self):
    print "Hi, my name is %s!" % self.name
    

def main():  
  c = Critter()
  c.name = "George"
  c.sayHi()
  
#this code only runs main when this file is run
#if the file is used as a module, main does not
#run
if __name__ == "__main__":
  main()



