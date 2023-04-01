""" helloBroken.py
    illustrate form IO
    Using functions causes problems
    sayHi doesn't know what lblOutput is!
    This program will not work!
"""

from tkinter import *

def sayHi():
  name = txtInput.get()
  lblOutput["text"] = "Hi there, %s!" % name

def main():
  app = Tk()
  lblOutput = Label(app, text = "type your name")
  lblOutput.grid()
  
  txtInput = Entry(app)
  txtInput.grid()
  
  btnClickMe = Button(app, text = "Click Me")
  btnClickMe.grid()
     
  btnClickMe["command"] = sayHi
 
  app.mainloop()

if __name__ == "__main__":
  main()
