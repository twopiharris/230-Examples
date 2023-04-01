from Tkinter import *

class TicTac(Tk):
  def __init__(self):
    Tk.__init__(self)
    
    #create buttons in a display
    self.btns = []
    
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
    self.mainloop()

  def click(self, i):
    curBtn = self.btns[i]
    oldVal = curBtn["text"]
    if oldVal == " ":
      curBtn["text"] = self.currentPlayer
      self.checkForWin()
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

def main():
  tt = TicTac()
      
if __name__ == "__main__":
  main()