""" HiUserTK
    uses the TK interface to make
    a GUI HI User program """

from Tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Hi, user")
        self.frame = Frame(self)
        self.frame.grid()
        self.lblOutput = Label(self.frame, text = "type your name")
        self.lblOutput.grid()
        self.txtInput = Entry(self.frame)
        self.txtInput.grid()
        self.btnClickMe = Button(self.frame,
                                 text = "click me",
                                 command = self.click)
        self.btnClickMe.grid()

    def click(self):
        userName = self.txtInput.get()
        self.lblOutput["text"] = "Hi, %s!" % userName

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()

    
        
