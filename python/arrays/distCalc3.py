""" distCalc3.py
    calculate distance with a 2d
    list
    Modded for python 3.4"""
    
def getCity(title):
  keepGoing = True
  while (keepGoing):
    print ("""  
    {}
    0) Indianapolis
    1) New York
    2) Tokyo
    3) London
    """.format(title))
    cityNum = input("City: ")
    if cityNum in ("0", "1", "2", "3"):
      keepGoing = False
    else:
      print("That is not a correct input. Please try again")

  return int(cityNum)

cityName = ("Indianapolis",
            "New York",
            "Tokyo",
            "London")

distance = (
  (0, 648, 6467, 4000),
  (648, 0, 6760, 3470),
  (6476, 6760, 0, 5956),
  (4000, 3470, 5956, 0)
)

fromID = getCity("Traveling from...")
toID = getCity("Traveling to...")
result = distance[fromID][toID]

print ("Distance from {} to {} is {} miles".format(cityName[fromID], cityName[toID], result))