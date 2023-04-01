from Tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.canvas = Canvas(self, width = 200, height = 200, bg = "white")
        self.canvas.grid()
        
        self.canvas.create_rectangle(0, 0, 100, 100, fill = "red")
        
        self.lblOut = Label(self, text = "Hi there..." )
        self.lblOut.grid()
        
        self.mainloop()
        
def main():
    app = App()
    
if __name__ == "__main__":
    main()
    
    
        

"""

root = Tk()
canvas = Canvas(root,width=200,height=200,bg="white")
canvas.grid()
firstRect = canvas.create_rectangle(0,0,10,10,fill="red")
secondRect = canvas.create_rectangle(5,5,15,15,fill="blue")

lblOut = Label(root, text = "Hi there")
lblOut.grid()



root.mainloop()
"""
