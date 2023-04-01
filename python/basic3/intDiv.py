""" integer division
    explains integer division in Python 3
"""

#by default, dividing integers produces a floating value

print("{} / {} = {}".format(10, 3, 10 / 3))

#but sometimes you really want an integer result...
#use the // to force integer division:

print("{} // {} = {}".format(10, 3, 10 // 3))

#integer division is incomplete.  Use modulus (%) for remainder

print("{} / {} = {} remainder {}".format(10, 3, 10 // 3, 10 % 3))

