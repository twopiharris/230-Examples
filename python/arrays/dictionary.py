""" dictionary.py
    demostrates dictionaries
"""

#you can add keys and values to a dictionary
#dictionary is denoted by curly braces ({})

stateCap ={
  "Illinois": "Springfield",
  "Indiana": "Indianapolis",
  "Wisconsin": "Madison"
}

#add an element to a dictionary with array-like syntax
stateCap["Florida"] = "Tallahassee"

#return an arbitrary value with the key:
print stateCap["Wisconsin"]

#use a loop to iterate through keys
for state in stateCap:
  #order of dictionary items is not specified
  print "%-15s %-15s" % (state, stateCap[state]);
  
print
print

#iteritems creates a cleaner interface to dictionary elements
for state, cap in stateCap.iteritems():
  print "%-15s %-15s" % (state, cap);
