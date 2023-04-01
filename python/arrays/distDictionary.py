""" distDictionary.py
    Use a dictionary to look up a 2D value
"""

cityName = ("Indianapolis",
            "New York",
            "Tokyo",
            "London")

distance = {
  "Indianapolis": {
    "Indianapolis": 0,
    "New York": 648,
    "Tokyo": 6467,
    "London": 4000 },
  "New York": {
    "Indianapolis": 648,
    "New York": 0,
    "Tokyo": 6760,
    "London": 3470 },
  "Tokyo": {
    "Indianapolis": 6476,
    "New York": 6760,
    "Tokyo": 0,
    "London": 5956 },
  "London": {
    "Indianapolis": 4000,
    "New York": 3470,
    "Tokyo": 5956,
    "London":0}
}

def getCity(title):
  
  keepGoing = True
  while (keepGoing):
    print title
    print "  (cities I know):"
    for theCity in cityName:
      print "    %s" % theCity
      
    city = raw_input("City name: ")
    if city in cityName:
      keepGoing = False
    else:
      print "That is not a correct input. Please try again"

  return city

fromCity = getCity("Traveling from...")
toCity = getCity("Traveling to...")
result = distance[fromCity][toCity]

print "Distance from %s to %s is %d miles" \
      % (fromCity, toCity, result)
