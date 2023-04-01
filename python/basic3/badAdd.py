""" baddAdd.py
    Tries to demonstrate adding to values input from the user
    Will not work correctly
    THIS PROGRAM HAS A DELIBERATE ERROR - see intAdd.py
    for a working version, and a complete explanation in the book
    Andy Harris
    3/20/06
    """

x = input("Please tell me the first number: ")
y = input("Please tell me the second number: ")

result = x + y

#print x, "+", y, "=", result
print("{} + {} = {}".format(x, y, result))
print("uh-oh...  Something's not right...")
