""" exceptions.py
    demonstrate exception-handling
    
"""

def loopedInput():
  """ keepg trying until you get a legitimate value """
  keepGoing = True
  while keepGoing:
    keepGoing = False
    try:
      x = int(input("please enter a number: "))
    except (ValueError):
      print ("That was not a number. Please try again")
      keepGoing = True
  
def main():
  try:
    x = input("please enter a number: ")
    x = int(x)
    y = 10 / x
    
  except (ValueError):
    print ("Can't convert to integer")
    x = 0
    y = 0
  except (ZeroDivisionError):
    print ("Can't divide by zero")
    x = 0
    y = 0
  except:
    print ("something went wrong")
    print (sys.exc_info())
    
  print ("x:", x)
  print ("y:", y)
  
  loopedInput()
  

if __name__ == "__main__":
  main()
