""" intAdd.py
    Uses type conversion to create a better
    adder.  This one converts all data to strings
    Andy Harris
    3/21/06 """

x = raw_input("First number: ")
y = raw_input("Second number: ")

x = int(x)
y = int(y)

result = x + y
print "%d + %d = %d" % (x, y, result)
