""" helloTK.py
    basic Hello World with Tkinter UI
    uses procedural approach
"""

from Tkinter import *
app = Tk()
lblOutput = Label(app, text = "Hi there")
lblOutput.grid()
app.mainloop()

