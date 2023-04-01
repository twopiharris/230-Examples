""" changeMaker.py
    get a price from user
    and an amount paid.
    determine how much change to give
    break change into twenties, tens ... etc

"""

#get a price from the user
price = raw_input("please tell me the price of the item: ")

#get an amount paid from the user
paid = raw_input("please tell me how much the user paid: ")

#convert all values to pennies
price = int(float(price) * 100)
paid = int(float(paid) * 100)

print "price: %d" % price
print "paid: %d" % paid

change = paid - price

print "Change due: %d " % change

twenties = change / 2000
print "twenties: %d" % twenties
change = change % 2000

tens = change / 1000
print "tens: %d" % tens
change = change % 1000

fives = change / 500
print "fives: %d" % fives
change = change % 500

ones = change / 100
print "ones: %d" % ones
change = change % 100

quarters = change / 25
print "quarters: %d" % quarters
change = change % 25

dimes = change / 10
print "dimes: %d" % dimes
change = change % 10

nickels = change / 5
print "nickels: %d" % nickels
change = change % 5

print "pennies: %d" % change
