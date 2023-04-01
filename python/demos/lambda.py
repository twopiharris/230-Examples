#-------------------------------------------------------------------------------
# Name:        lambda
# Purpose:      Lambda demo
#
# Author:      Andy
#
# Created:     11/12/2011
# Copyright:   (c) Andy 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Tkinter import *

class Counter(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.lblOutput= Label(self, text = "output")
        self.lblOutput.grid()
        
        #use lambda to 'package' a literal value into a command
        Button(self, text = "One", command = lambda: self.say(1)).grid()
        Button(self, text = "Two", command = lambda: self.say(2)).grid()
        Button(self, text = "Three", command = lambda: self.say(3)).grid()
        self.mainloop()

    def say(self, number):
        if number == 1:
            result = "uno"
        elif number == 2:
            result = "dos"
        elif number == 3:
            result = "tres"
        else:
            result = "I don't know"
        self.lblOutput["text"] = result



def main():
    counter = Counter()

if __name__ == '__main__':
    main()
