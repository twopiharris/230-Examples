""" CRUD.py
    demonstrates the CRUD features in a basic database
    C - Create
    R - Report
    U - Update
    D - Delete
    S - Search
"""

import sqlite3
#import pdb

#build connection to database
#console and cursor objects are global
conn = sqlite3.connect("practice.db")
c = conn.cursor()

def main():
  keepGoing = True
  while keepGoing:
    result = menu()
    if result == "0":
      keepGoing = False
    elif result == "1":
      buildDefault()
    elif result == "2":
      createRecord()
    elif result == "3":
      reportAll()
    elif result == "4":
      updateRecord()
    elif result == "5":
      deleteRecord()
    elif result == "6":
      searchName()
    else:
      print("I don't understand. Please try again...")

  # close connection to database when project finished
  c.close()


def menu():
  print ("""
  0) Quit
  1) Build default
  2) Create a contact
  3) Report all records
  4) Update a record
  5) Delete a record
  6) Search for a record by name
  """)

  result = input("What will you do? ")
  return result

def buildDefault():
  """ build and populate the table for the
      first time

      Note this function destroys and rebuilds the database.
      Great for practice, not good in 'real life.'

  """

  #create a table
  c.execute("DROP TABLE IF EXISTS contacts")
  sql = """
  CREATE TABLE contacts (
  id INTEGER PRIMARY KEY,
  name VARCHAR(20),
  company VARCHAR(20),
  email VARCHAR(20)
  ) """
  c.execute(sql)

  #insert records into the table - note placeholders
  c.execute("INSERT INTO contacts VALUES (null, ?, ?, ?)",
            ('Andy Harris', 'IUPUI', 'aharris@cs.iupui.edu'))
  c.execute("INSERT INTO contacts VALUES (null, ?, ?, ?)",
            ('Bill Gates', 'Microsoft', 'bill@vista.com'))
  c.execute("INSERT INTO contacts VALUES (null, ?, ?, ?)",
            ('Steve Jobs', 'Apple', 'steve@newton.com'))

  # must commit to ensure saves are changed
  conn.commit()

def createRecord():
  """ ask for all information and build a new record
      note: never allow user to input ID - this can lead to collisions
  """
  name = input("Name: ")
  company = input("Company: ")
  email = input("Email: ")

  c.execute("INSERT INTO contacts VALUES(null, ?, ?, ?)",(name, company, email))
  conn.commit()

def reportAll():
  """ report each record in the table """

  #view the results
  result = c.execute("SELECT * FROM contacts")

  #get the field names - cool list comprehension
  names = [description[0] for description in result.description]

  for record in result:
    fieldNum = 0
    for field in record:
      print ("{:10}: {}".format(names[fieldNum], field))
      fieldNum += 1
    print ("")

    # commit is not necessary as we did not change the database

def updateRecord():
  """ get a record number, display current value of record, allow values to
      be changed """

  rn = getRecordID()
  if rn == 0:
    # getRecord function will send 0 on failure. Never use an untested ID
    print ("Not a legal ID. Please try again")
  else:
    result = c.execute("SELECT * FROM contacts WHERE id = ?",(rn))
    for row in result:
      newName = input ("Name ({}): ".format(row[1]))
      if newName == '':
        newName = row[1]

      newCompany = input("Company ({}): ".format(row[2]))
      if newCompany == '':
        newCompany = row[2]

      newEmail = input("Email ({}): ".format(row[3]))
      if newEmail == '':
        newEmail = row[3]

    c.execute ("""UPDATE contacts
                  SET
                    name = ?,
                    company = ?,
                    email = ?
                  WHERE
                    id = ?""",
                    (newName, newCompany, newEmail, rn))
    conn.commit()

def deleteRecord():
  """ get a record ID, deletes that record """
  rn = getRecordID()
  if rn == 0:
    print("Not a valid record. Please try again")
  else:
    result = c.execute("SELECT * FROM contacts WHERE id = ?", (rn))
    for row in result:
      print("Name: {}".format(row[1]))
      print("Company: {}".format(row[2]))
      print("Email: {}".format(row[3]))


    """ NEVER do a deletion without a confirmation.
        NEVER EVER do a deletion without a WHERE clause
        An Empty WHERE clause will efficiently delete the entire table!!!"""

    confirmation = input("Are you sure you want to delete this record? (Y/N)")
    confirmation = confirmation.upper()
    if confirmation.startswith("Y"):
      c.execute("DELETE FROM contacts WHERE ID = ?", (rn))
      print("record deleted")

def searchName():
  """ asks for a name.  Searches the database for a similar name using the
      LIKE clause """
  searchName = input("Name to search for: ")

  print()
  # You have to be a little sneaky with wildcards and placeholders...
  result = c.execute("SELECT * FROM contacts WHERE name LIKE ?",("%"+searchName+"%",))
  for row in result:
    print ("Name: {}".format(row[1]))
    print("Company: {}".format(row[2]))
    print("Email: {}".format(row[3]))
    print()

def getRecordID():
  """ utility function: Lists all current records, allows user to choose an ID
      returns that ID or 0 if not found or cancelled """
  result = c.execute("SELECT id, name FROM contacts")

  print()
  #create empty list of current IDs
  legalIDs = []
  for row in result:
    id = row[0]
    name = row[1]
    print("{}: {}".format(id, name))

    #add current ID to list of legal IDs
    legalIDs.append(id)

  print()
  returnVal = input("Which user #? (or 0 to cancel) ")

  #be sure it's really a digit
  if not returnVal.isdigit():
    print("ID must be a digit")
    returnVal = 0

  #ensure returnVal is one of the legal IDs
  if int(returnVal) not in legalIDs:
    returnVal = 0


  return returnVal

if __name__ == "__main__":
  main()
