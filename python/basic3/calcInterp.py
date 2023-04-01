""" calculator.py
    given any two values, calculates
    the sum, difference, product, and
    quotient of those two values
    3/20/06 """

x = raw_input("first number: ")
y = raw_input("second number: ")

x = float(x)
y = float(y)

print ("%.2f + %.2f = %.2f") % (x, y, x + y)
print ("%.2f - %.2f = %.2f") % (x, y, x - y)
print ("%.2f * %.2f = %.2f") % (x, y, x * y)
print ("%.2f / %.2f = %.2f") % (x, y, x / y)
