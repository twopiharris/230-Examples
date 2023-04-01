""" scope.py
    illustrates scope and functions
    """

varOutside = "I was created outside the function"
print("outside the function, varOutside is: {}".format(varOutside))

def theFunction():
    varInside = "I was made inside the function"

    print("inside the function, varOutside is: {}".format(varOutside))
    print("inside the function, varInside is: {}".format(varInside))

theFunction()

print("back outside the function, varOutside is: {}".format(varOutside))
# if I uncomment the next line, the program will crash
#print("back outside the function, varInside is: {}".format(varInside))

