""" sudoku.py
    generate a simple completed sudoku puzzle

"""
import random

ROWS = 9
COLS = 9

puzzle = []

def buildBlankPuzzle():
  global puzzle
  #generate blank puzzle
  puzzle = []
  for r in range(ROWS):
    puzzle.append([])
    for c in range(COLS):
      puzzle[r].append(0)

def showPuzzle():
  for r in range(ROWS):
    for c in range(COLS):
      print puzzle[r][c],
    print
  print

def uniqueInRow(val, r):
  #given a value, row r.  determine if the value is unique in that row
  #if the value already exists in row, return false, otherwise return true

  unique = True
  for c in range(COLS):
    if val == puzzle[r][c]:
      unique = False
  return unique
   
def uniqueInCol(val, c):
  #given a value, col c,  determine if the value is unique in that col
  #if the value already exists in col, return false, otherwise return true

  unique = True
  for r in range(ROWS):
    if val == puzzle[r][c]:
      unique = False
  return unique


def populate():
  itWorked = True
  for r in range(ROWS):
    for c in range(COLS):
      #print "r: %d, c: %d" % (r, c)
      keepGoing = True
      while keepGoing:
        val = random.randint(1,9)
        if uniqueInRow(val, r):
          if uniqueInCol(val, c):
            puzzle[r][c] = val
            keepGoing = False
        
        #if it's impossible, give up
        if not uniqueInRow(val, r):
          if not uniqueInCol(val, c):
            keepGoing = False
            itWorked = False

        """
        #print puzzle if we're on row 8 and col 8
        if r == 8:
          if c == 8:
            keepGoing = False
            itWorked = True
        """


  return itWorked

def makePuzzle():
  """run the populate function until you get a working grid"""

  keepGoing = True
  while keepGoing:
    if populate() == True:
      keepGoing = False

def main():
  buildBlankPuzzle()
  showPuzzle()
  makePuzzle()
  showPuzzle()

if __name__ == "__main__":
  main()


