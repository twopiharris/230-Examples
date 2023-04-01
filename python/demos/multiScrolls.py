""" multiScrolls.py
    Demonstrate three scroll bars add to 100
    change top scroll, bottom two change 
    proportionately """

from Tkinter import *

class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    self.scrA = Scale(self, from_ = 0, to = 100, orient = HORIZONTAL)
    self.scrA.grid()
    self.scrA.set(0)
    self.scrA["command"] = self.adjustScrollers

    self.scrB = Scale(self, from_ = 0, to = 100, orient = HORIZONTAL)
    self.scrB.grid()
    self.scrB.set(50)

    self.scrC = Scale(self, from_ = 0, to = 100, orient = HORIZONTAL)
    self.scrC.grid()
    self.scrC.set(50)

    self.mainloop()

  def adjustScrollers(self, aVal):
    aVal = int(aVal)
    amountToSpend = 100 - aVal

    #read in as ints
    currentB = int(self.scrB.get())
    currentC = int(self.scrC.get())
    #now convert those ints to floats
    #can't read directly as floats!
    currentB = float(currentB)
    currentC = float(currentC)

    print "Before: currentB: %.2f, currentC: %.2f" % (currentB, currentC)

    bcTotal = currentB+currentC
    bPerc = currentB / bcTotal
    cPerc = currentC / bcTotal

    newB = 100 - (currentB + (bPerc * amountToSpend))
    newC = 100 - (currentC + (cPerc * amountToSpend))

    
    total = aVal + newB + newC
    print "bPerc: %.2f, cPerc: %.2f, Total: %d" % (bPerc, cPerc, total)
    print "amountToSpend: %d, newB: %.2f, newC: %.2f" % (amountToSpend, newB, newC)
    print

    self.scrB.set(newB)
    self.scrC.set(newC)
    

def main():
  app = App()

if __name__ == "__main__":
  main()
