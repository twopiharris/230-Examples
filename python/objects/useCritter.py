""" useCritter
    illustrates default namespace
    requires 'critter.py' to be in same directory

"""
from critter import *
c = Critter()
#there's only one critter defined here, with a default name
print c.name
#however, you'll see two print statements!

#importing critter.py causes its main() function to run



