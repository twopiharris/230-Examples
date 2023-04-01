""" pickleDemo.py
    demonstrates object serialization
    with pickle """
    
import cPickle
    
class Critter(object):
  def __init__(self, name = "", age = 0):
    object.__init__(self)
    self.name = name
    self.age = age   
    
def main():
  c = Critter("Lizzie Borden", 23)
  file = open("serialKiller.dat", "w")
  cPickle.dump(c, file)
  file.close()
  
  file = open("serialKiller.dat", "r")
  
  d = cPickle.load(file)
  print d.name
  
  #save an entire list at once
  badCritters = [
    Critter("Darth Vader", 65),
    Critter("Knight who says 'Nii'", 43)
  ]

  file = open("badGuys.dat", "w")
  cPickle.dump(badCritters, file)
  file.close()
  
  #load them back in
  file = open("badGuys.dat", "r")
  otherGuys = cPickle.load(file)
  for guy in otherGuys:
    print guy.name
  
if __name__ == "__main__":
  main()