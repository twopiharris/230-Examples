""" nameGame.py
    illustrate basic string functions
    Andy Harris """


userName = input("Please tell me your name: ")
print ("I will shout your name: ", userName.upper())
print ("Now all in lowercase: ", userName.lower())
print ("How about inverting the case? ", userName.swapcase())
numChars = len(userName)
print ("Your name has", numChars, "characters")
print ("Now I'll pronounce your name like a cartoon character:")
userName = userName.upper()
userName = userName.replace("R", "W")
userName = userName.title()
print (userName)
