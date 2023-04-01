""" timing.py
    demonstrates use of after method
    for timing in Tkinter
"""

from Tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.lblOut = Label(text = "0")
        self.lblOut.grid()
        
        self.counter = 0
        
        self.update()
        self.mainloop()
        
    def update(self):
        self.counter += 1
        self.lblOut["text"] = self.counter
    
        #after 100 milliseconds, repeat this function
        #NOT recursive!!
        self.after(100, self.update)
    
def main():
    app = App()
    
if __name__ == "__main__":
    main()
    
    