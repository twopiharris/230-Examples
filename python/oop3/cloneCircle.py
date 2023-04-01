""" cloneCircle.py
    Illustrates basic
    inheritance
"""

from circleProperty import *

class Clone(Circle):
  pass

def main():
  c = Clone(30)
  print(c.diameter)
  
if __name__ == "__main__":
  main()
