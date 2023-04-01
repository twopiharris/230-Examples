""" exceptDemo.py """
import sys

keepGoing = True
while keepGoing:
    #begin with the assumption everything went well
    keepGoing = False
    try:
        number = input("please enter a number: ")
        number = int(number)
        print(10 / number)

    except ValueError:
        print("not an integer")
        print(sys.exc_info())
        keepGoing = True
        
    except ZeroDivisionError:
        print("can't divide by zero")
        print(sys.exc_info())
        keepGoing = True
        
    except:
        print("Something went wrong")
        print(sys.exc_info())
        keepGoing = True
        

