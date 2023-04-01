""" textEdit.py
    a simple text editor in python / tkinter
"""

from tkinter import *
import tkinter.filedialog

class Editor(Tk):
  def __init__(self):
    Tk.__init__(self)
    self.title("Text editor")
    
    menubar = Menu(self, tearoff = 0)
    self.config(menu = menubar)

    fileMenu = Menu(menubar)
    menubar.add_cascade(label = "File", menu = fileMenu)
    
    fileMenu.add_command(label = "New", command = self.new)
    fileMenu.add_command(label = "Save As", command = self.saveAs)
    fileMenu.add_command(label = "Open", command = self.open)
    fileMenu.add_command(label = "Exit", command = self.quit)
    
    self.textArea = Text(self)
    self.textArea.grid()
    
    self.mainloop()
    
  def new(self):
    self.textArea.delete(1.0, END)
    
  def saveAs(self):
    file = tkinter.filedialog.asksaveasfile()
    content = self.textArea.get(1.0, END)
    file.write(content)
    file.close()
    
  def open(self):
    file = tkinter.filedialog.askopenfile()
    text = ""
    for line in file:
      text += line
      
    self.new()
    self.textArea.insert(1.0, text)
    file.close()
  
def main():
  e = Editor()
  
if __name__ == "__main__":
  main()
  
