#-------------------------------------------------------------------------------
# Name:        lambdaVar.py
# Purpose:      Lambda demo with variables
#
# Author:      Andy
#
# Created:     11/12/2011
#-------------------------------------------------------------------------------

from Tkinter import *

class Counter(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.lblOutput= Label(self, text = "Click for Japanese")
        self.lblOutput.grid()
        self.btns = []
        self.english= ("one", "two", "three")
        self.japanese = ("ichi", "ni", "san")
        for i in range(len(self.english)):
            self.btns.append(Button(self, text = self.english[i]))
            self.btns[i]["command"] = lambda i = i: self.say(i)
            self.btns[i]["anchor"] = "center"
            self.btns[i]["width"] = 30
            self.btns[i].grid(sticky = "we")

        self.mainloop()

    def say(self, number):
        self.lblOutput["text"] = self.japanese[number]

def main():
    counter = Counter()

if __name__ == '__main__':
    main()
