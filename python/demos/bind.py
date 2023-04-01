#bind.py

from Tkinter import *

class Bind(Tk):
  def __init__(self):
    Tk.__init__(self)
    self.lblOut = Label(self, text = "press a button")
    self.btnOne = Button(self, text = "one", width = 20)
    self.btnTwo = Button(self, text = "two", width = 20)
    self.btnThree = Button(self, text = "three", width = 20)

    self.lblOut.grid()
    self.btnOne.grid(sticky = "ew")
    self.btnTwo.grid(sticky = "ew")
    self.btnThree.grid(sticky = "ew")


    #binding a mouse button press
    #<Button-1> is the left mouse button
    self.btnOne.bind("<Button-1>", self.handler)
    self.btnTwo.bind("<Button-1>", self.handler)
    self.btnThree.bind("<Button-1>", self.handler)

    self.mainloop()

  def handler(self, event):
    theButton = event.widget
    if theButton == self.btnOne:
      self.lblOut["text"] = "button one"
    elif theButton == self.btnTwo:
      self.lblOut["text"] = "button two"
    elif theButton == self.btnThree:
      self.lblOut["text"] = "button three"
    else:
      self.lblOut["text"] =  "Some other button"

bind = Bind()
