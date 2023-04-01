""" crypto.py
    Implements a simple substitution cypher
"""

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"

def main():
  keepGoing = True
  while keepGoing:
    response = menu()
    if response == "1":
      plain = raw_input("text to be encoded: ")
      print encode(plain)
    elif response == "2":
      coded = raw_input("code to be decyphered: ")
      print decode(coded)
    elif response == "0":
      print "Thanks for doing secret spy stuff with me."
      keepGoing = False
    else:
      print "I don't know what you want to do..."

def menu():
  print """
  
  SECRET DECODER MENU
  
  0) Quit
  1) Encode
  2) Decode
  """
  response = raw_input("What do you want to do? ")
  return response

def encode(plain):
  #start with an empty output variable
  output = ""
  
  #convert plain to all uppercase
  plain = plain.upper()
  #loop through each character in plain
  for currentChar in plain:
    #look at the current character
    
    #find the position of that character in the alphabet
    charPos = alpha.find(currentChar)
    
    #ignore anything not in the alphabet
    if charPos != -1:
      #find the corresponding character in the key
      newChar = key[charPos]
      
      #debug output
      #print "%s, %d, %s" % (currentChar, charPos, newChar)
      
      #add the key character to the end of the output
      output += newChar
    
  #return the output
  return output

def decode(coded):
  #start with an empty output variable
  output = ""
  
  #convert coded to all uppercase
  coded = coded.upper()
  #loop through each character in plain
  for currentChar in coded:
    #look at the current character
    
    #find the position of that character in the key
    charPos = key.find(currentChar)
    
    #ignore anything not in the alphabet
    if charPos != -1:
      #find the corresponding character in the alphabet
      newChar = alpha[charPos]
      
      #debug output
      #print "%s, %d, %s" % (currentChar, charPos, newChar)
      
      #add the key character to the end of the output
      output += newChar
    
  #return the output
  return output

if __name__ == "__main__":
  main()
