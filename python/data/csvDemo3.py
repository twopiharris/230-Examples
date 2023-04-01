""" csvDemo.py
    reading content from comma-seperated values (CSV) files
    expects contacts.csv to have name, company, email
    one record per line
"""

file = open("contacts.csv", "r")
for line in file:
  currentLine = line.split(",")
  (name, company, email) = currentLine
  print ("Name:   {} ".format(name))
  print ("Company: {}".format(company))
  print ("Email:   {}".format(email))
  print()
  
file.close()
