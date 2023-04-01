""" interpolation.py
    demonstrates variable interpolation
    """

name = input("Hi, what's your name? ")

prompt = "How old are you, {}? ".format(name)

age = input(prompt)
age = int(age)

print("{} is {} years old".format(name, age))

#reverse the order
print("{1} is {0} years old".format(name, age))

#print in other bases
print("{} is {:b} years old in binary".format(name, age))
print("{} is {:o} years old in octal".format(name, age))
print("{} is {:X} years old in hexadecimal".format(name, age))

#force to floating notation
print("{} is {:f} years old".format(name, age))
print("{} is {:.2f} years old".format(name, age))

#set width
print("|{:20}|".format(name))

#justify
print("|{:<20}|".format(name))
print("|{:>20}|".format(name))
print("|{:^20}|".format(name))

