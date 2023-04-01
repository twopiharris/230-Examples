""" 
    Ask the user for a price, tendered amount
    determine how much change is due.  Convert that value
    to a number of pennies. Figure out how many twenties the
    program needs to return, and how much change is left after 
    accounting for the twenties.  Repeat for other denomination.
"""

# create an int variable called price
# create an int variable called tendered
# create an int for changeDue

# input "price" as float -> fPrice
fPrice = input("Price: ")

# convert fPrice * 100 to int -> price
price = int(fPrice * 100)

# input "tendered" as float -> fTendered
fTendered = input("Tendered: ")

# convert fTenderd *100 to int -> tendered
tendered = int(fTendered * 100)

# subtract price from tendered -> changeDue
changeDue = tendered - price

print("price: {}".format(price))
print("tendered: {}".format(tendered))
print("due {}".format(changeDue))


# determine how many twenties to return -> twenties
twenties = changeDue // 2000

# determine what's left in change due after compensating for twenties
changeDue = changeDue % 2000

# repeat for other denominations

tens = changeDue // 1000
changeDue = changeDue % 1000

fives = changeDue // 500
changeDue = changeDue % 500


#print out results

print("Twenties: {}".format(twenties))
print("Tens: {}".format(tens))
print("Fives: {}".format(fives))


