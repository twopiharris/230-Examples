""" imageDemo.py
    demonstrates using images in Tkinter
"""

from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        #photoImage file type must be gif or pgm !!?!
        #convert and resize in image editor as needed
        #be sure to save each image as a member variable
        #this prevents a garbage-collection bug
        self.imgCow = PhotoImage(file = "cow.gif")
        
        self.lblImage = Label(self, image = self.imgCow)
        self.lblImage.grid()
        self.lblCaption = Label(self, text = "Cow")
        self.lblCaption.grid()
        
        self.mainloop()
        
def main():
    a = App()
    
if __name__ == "__main__":
    main()
    