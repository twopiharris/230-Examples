""" intAdd.py
    Uses type conversion to create a better
    adder.  This one converts all data to strings
    Andy Harris
    3/21/06 """

x = input("First number: ")
y = input("Second number: ")

x = int(x)
y = int(y)

result = x + y
print("{} + {} = {}".format(x, y, result))




