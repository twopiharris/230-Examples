""" readFile.py
    read the contents of a text file
"""

file = open("groceries.txt", "r")
for line in file:
  print (line.strip())
    
