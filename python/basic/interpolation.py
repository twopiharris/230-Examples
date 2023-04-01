""" interpolation.py
    demonstrates variable interpolation
    """

name = raw_input("Hi, what's your name? ")

prompt = "How old are you, %s? " % name

age = raw_input(prompt)
age = int(age)

decades = age / 10.0
print decades

print "%s is %d years old." % (name, age)
print "That is %.2f decades" % decades

