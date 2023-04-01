""" anim.py
    basic animation with Tk and timer

"""

from Tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Basic animation loop")
        self.HEIGHT = 400
        self.WIDTH = 600
        
        self.canvas = Canvas(self, height = self.HEIGHT,
                             width = self.WIDTH, bg = "white")
        self.canvas.grid()
        
        #rectangle properties
        self.r_x = 10
        self.r_y = 200
        self.r_width = 25
        self.r_height = 25
        
        self.update()
        self.mainloop()
        
    def clear(self):
        #clear canvas
        self.canvas.create_rectangle(0, 0, self.WIDTH,
                                     self.HEIGHT, fill = "white")
        
    def update(self):
        
        #increment x
        self.r_x += 5
        #check for border
        if self.r_x > self.WIDTH:
            self.r_x = 0
        
        #clear background
        self.clear()
        
        #draw rectangle on canvas
        self.canvas.create_rectangle(self.r_x, self.r_y,
                                     self.r_x + self.r_width,
                                     self.r_y + self.r_height,
                                     fill = "red")
        
        #repeat
        self.after(50, self.update)

def main():
    app = App()
    
if __name__ == "__main__":
    main()