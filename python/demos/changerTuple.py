""" changerTuple """

penniesLeft = 1234

currency = (
  ("twenties", 2000),
  ("tens", 1000),
  ("fives", 500),
  ("ones", 100),
  ("quarters", 25)
)


for line in currency:
  (denom, value) = line
  numTokens = penniesLeft / value
  penniesLeft = penniesLeft % value

  print denom, numTokens









