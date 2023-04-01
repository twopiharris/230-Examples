""" propertyDemo.py
    practice with the property tool
    __fName is a hidden variable
    It is accessed only through get and set methods
    but the firstName property provides access
"""

class Critter(object):
    def __init__(self, fName):
        self.firstName = fName
        
    def getFirstName(self):
        return self.__fName
    
    def setFirstName(self, fName):
        #setter can filter or modify input
        if fName.endswith(", Destroyer of Worlds"):
            self.__fName = fName
        else:
            self.__fName = fName + ", Destroyer of Worlds"
      
    firstName = property(fget = getFirstName, fset = setFirstName)

c = Critter("George")

print c.firstName
c.firstName = "Ralph"
print c.firstName

#the __fName attribute is hidden, so trying to display it
#directly will cause an error
print c.__fName


        
    
