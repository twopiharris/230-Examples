""" canvasDemo.py
"""

from tkinter import *

class CanvasDemo(Tk):
  def __init__(self):
    Tk.__init__(self)
    self.myCanvas = Canvas(self, height = 300, width = 300)
    self.myCanvas.grid()
    
    self.myCanvas.create_rectangle(10, 10, 200, 100, fill = "#ff0000")

    self.mainloop()

def main():
  cd = CanvasDemo()

if __name__ == "__main__":
  main()
