""" helloIO.py
    illustrate form IO
    (still procedural)
"""

from Tkinter import *

app = Tk()
lblOutput = Label(app, text = "type your name")
lblOutput.grid()

txtInput = Entry(app)
txtInput.grid()

btnClickMe = Button(app, text = "Click Me")
btnClickMe.grid()

def sayHi():
  name = txtInput.get()
  lblOutput["text"] = "Hi there, %s!" % name
  
btnClickMe["command"] = sayHi
# note no parens after sayHi
# treating function as a variable

app.mainloop()
