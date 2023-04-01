from Tkinter import *

class TicTac(Tk):
  def __init__(self):
    Tk.__init__(self)
    
    #create buttons in a display
    self.btns = []
    self.cellVals = [3,2,3,2,4,2,3,2,3]
  
    self.currentPlayer = "X"
    for i in range(9):
      self.btns.append(Button(self, text = " ",
                                    width = 3,
                                    command = lambda j = i: self.click(j)))
      self.btns[i].grid(row = i / 3, column = i % 3)

    self.winCbos = (
      (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
      (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
    )
    self.calcBest()
    
    self.mainloop()

  def click(self, i):
    curBtn = self.btns[i]
    oldVal = curBtn["text"]
    if oldVal == " ":
      curBtn["text"] = self.currentPlayer
      #make that cell unattractive
      self.cellVals[i] -= 100
      
      self.checkForWin()
      self.calcBest()

      if self.currentPlayer == "X":
        self.currentPlayer = "O"
      else:
        self.currentPlayer = "X"
    else:
      print "that square is taken"
      
  def checkForWin(self):
    for cbo in self.winCbos:
      (a, b, c) = cbo
      self.checkWin(a, b, c)
   
  def checkWin(self, a, b, c):
    aBtn = self.btns[a]
    aVal = aBtn["text"]
    bBtn = self.btns[b]
    bVal = bBtn["text"]
    cBtn = self.btns[c]
    cVal = cBtn["text"]
    
    if aVal == bVal:
      if aVal == cVal:
        if aVal != " ":
          print "WINNER: %s!" % aVal
  
  def calcBest(self):
    """ calculate the heuristic based on the current
        board and print out the best cell to take
    """
    #reset cellVals
    self.cellVals = [3,2,3,2,4,2,3,2,3]
   
    for cbo in self.winCbos:
      (a, b, c) = cbo
      self.checkCloseToWin(a, b, c)
        
    #find the highest cell number
    highestCell = 0
    highestVal = 0
    for cellNum in range(len(self.cellVals)):
      #make a cell unattractive if it currently has a value
      if self.btns[cellNum]["text"] != " ":
        self.cellVals[cellNum] -= 99
        
      #check to see if this is the highest value
      if self.cellVals[cellNum] > highestVal:
        highestCell = cellNum
        highestVal = self.cellVals[cellNum]
    
    self.printVals()
    print highestCell

  def checkCloseToWin(self, a, b, c):
    aBtn = self.btns[a]
    aVal = aBtn["text"]
    bBtn = self.btns[b]
    bVal = bBtn["text"]
    cBtn = self.btns[c]
    cVal = cBtn["text"]
    
    hotCell = None
    
    if aVal == bVal:
      if aVal != " ":
        if cVal == " ":
          self.cellVals[c] += 5
    
    if aVal == cVal:
      if aVal != " ":
        if bVal == " ":
          self.cellVals[b] += 5
        
    if bVal == cVal:
      if bVal != " ":
        if aVal == " ":
          self.cellVals[a] += 5
  
  def printVals(self):
    print """
    %3d, %3d, %3d
    %3d, %3d, %3d
    %3d, %3d, %3d
    """ % (self.cellVals[0], self.cellVals[1], self.cellVals[2],
           self.cellVals[3], self.cellVals[4], self.cellVals[5],
           self.cellVals[6], self.cellVals[7], self.cellVals[8])
    
def main():
  tt = TicTac()
      
if __name__ == "__main__":
  main()
