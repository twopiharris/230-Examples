""" password.py
    Ask the user for a password
    repeat until user gets it right
    or has tried three times """

keepGoing = True
correct = "Python"
tries = 3

while keepGoing:
    guess = input("Please enter the password: ")
    tries = tries - 1
    
    if guess == correct:
        print("You may proceed")
        keepGoing = False
    else:
        print("That's not correct.")

        if tries <= 0:
            print("Sorry.  You only had three tries")
            keepGoing = False
        else:
            print("You have {} tries left".format(tries))
        
