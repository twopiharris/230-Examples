""" widgetDemo.py
    TK widget demo
    Demonstrates all major TK widgets
"""

from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser


#from tkMessageBox import *
#import tkColorChooser
#import tkinter.colorchooser
#import tkinter.messagebox


class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    
    Label(self, text = "Button").grid(row = 0, column = 0)
    self.btnButton = Button(self, text = "Show Values", command = self.showVals)
    self.btnButton.grid(row = 0, column = 1)

    Label(self, text = "Checkbutton").grid(row = 1, column = 0)
    self.checkVar = IntVar()
    self.chkCheck = Checkbutton(self, text = "Check Button",
                                variable = self.checkVar)
    self.chkCheck.grid(row = 1, column = 1)

    Label(self, text = "Entry").grid(row = 2, column = 0)
    self.txtEntry = Entry(self)
    self.txtEntry.grid(row = 2, column = 1)
    
    Label(self, text = "Listbox").grid(row = 3, column = 0)
    self.lstList = Listbox(self, height = 3)
    self.lstList.grid(row = 3, column = 1)
    self.lstList.insert(END, "one", "two", "three")

    Label(self, text = "Text").grid(row = 4, column = 0)
    self.txtText = Text(self, height = 4, width = 25)
    self.txtText.grid(row = 4, column = 1)
    self.txtText.insert(1.0, "text \ngoes \nhere...")

    self.radVar = IntVar()
    Label(self, text = "Radio Buttons").grid(row = 5, rowspan = 2)
    self.radRadio1 = Radiobutton(self, text = "one", variable = self.radVar, value = 1)
    self.radRadio2 = Radiobutton(self, text = "two", variable = self.radVar, value = 2)
    self.radRadio1.grid(row = 5, column = 1)
    self.radRadio2.grid(row = 6, column = 1)
    
    #self = scrVar = IntVar()
    Label(self, text = "Scale").grid(row = 7, column = 0)
    self.scrScale = Scale(self, orient = HORIZONTAL, to = 255)
    self.scrScale.grid(row = 7, column = 1)
    
    Label(self, text = "Spinbox").grid(row = 8, column = 0)
    self.spnSpin = Spinbox(self, values = ("one", "two", "three"))
    self.spnSpin.grid(row = 8, column = 1)

    """
    taking this out.  it's a bit too much for this example
    
    Label(self, text = "Message Box").grid(row = 9, column = 0)
    self.btnMessage = Button(self, text = "click for dialogs")
    self.btnMessage["command"] = self.showMessage
    self.btnMessage.grid(row = 9, column = 1)
    """
    
    Label(self, text = "Top Level").grid(row = 10, column = 0)
    self.btnTop = Button(self, text = "click for new window")
    self.btnTop["command"] = self.showTop
    self.btnTop.grid(row = 10, column = 1)
    
    self.mainloop()
    
  """ no longer needed - see dialogs3.py for details
  def showMessage(self):
    showinfo("Info", "I'm an info box")
    result = askquestion("question", "Are we having fun yet?")
    showinfo("", "You said %s." % result)
    newColor = tkColorChooser.askcolor()
    self["bg"] = newColor[1]
  """
    
  def showTop(self):
    self.newWindow = Toplevel(self)
    Label(self.newWindow, text = "Hi there").grid()
    self.newWindow.grid()
    
  def showVals(self):
    """ demonstrate how to get copy from the major elements """
    #get a value from the check box
    if self.checkVar.get() == 1:
      print("checkbox is checked")
    else:
      print("checkbox is not checked")
      
    #get a value from an entry field
    print("Entry contains this: ()".format(self.txtEntry.get()))
    
    #get the currently selected item in the list box
    selected = self.lstList.curselection()
    if selected == ():
      print("nothing selected")
    else:
      selValue= self.lstList.get(selected[0])
      print("List box: {}) {}".format(selected[0], selValue))
    
    #get the contents of the text area
    print("text:")
    print(self.txtText.get(1.0, END))
    
    #get the radio button value
    print("radio: {}".format(self.radVar.get()))
    
    #get the scale's value
    print("scale: {}".format(self.scrScale.get()))
    
    #get the spinbox's value
    print("spin: {}".format(self.spnSpin.get()))
    
def main():
  app = App()
  
if __name__ == "__main__":
  main()
