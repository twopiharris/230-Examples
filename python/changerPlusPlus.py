""" changerPlusPlus.py
    improve changer with tuples
"""

changeDue = 1234
penniesLeft = changeDue


moneyData = (
  ("twenties", 2000),
  ("tens", 1000),
  ("fives", 500),
  ("ones", 100),
  ("quarters", 25),
  ("dimes", 10),
  ("nickels", 5),
  ("pennies", 1)
)

for denom in moneyData:
  (curName, value) = denom

  currentVal = penniesLeft // value
  penniesLeft = penniesLeft % value

  print "%s: %d" % (curName, currentVal)


