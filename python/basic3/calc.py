""" calculator.py
    given any two values, calculates
    the sum, difference, product, and
    quotient of those two values
    3/20/06 """

x = input("first number: ")
y = input("second number: ")

x = float(x)
y = float(y)

sum = x + y
difference = x - y
product = x * y
quotient = x / y

"""
print x, "+", y, "=", sum
print x, "-", y, "=", difference
print x, "*", y, "=", product
print x, "/", y, "=", quotient
"""

print("{:.2f} + {:.2f} = {:.2f}".format(x, y, sum))
print("{:.2f} - {:.2f} = {:.2f}".format(x, y, difference))
print("{:.2f} * {:.2f} = {:.2f}".format(x, y, product))
print("{:.2f} / {:.2f} = {:.2f}".format(x, y, quotient))
