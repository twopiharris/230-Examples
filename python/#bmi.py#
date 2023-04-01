"""bmi.py """

from Tkinter import *

class App(object):
  def __init__(self, master):
    self.frame = Frame(master)
    self.frame.grid()

    master.title("Body Mass Indicator")

    self.lblWeight = Label(self.frame,
                           text = "Weight in pounds",
                           fg = "white",
                           bg = "blue")
    self.lblWeight.grid(row = 0, column = 0, sticky = "ew")
    self.txtWeight = Entry(self.frame)
    self.txtWeight.grid(row = 0, column = 1)
    self.txtWeight.insert(INSERT, "180")
        
    self.lblFeet = Label(self.frame,
                         text = "Height in feet",
                         fg = "white",
                         bg = "blue")
    self.lblFeet.grid(row = 1, column = 0, sticky = "ew")
    self.txtFeet = Entry(self.frame)
    self.txtFeet.grid(row = 1, column = 1)
    self.txtFeet.insert(INSERT, "6")
    
    self.lblInches = Label(self.frame,
                           text = "Height in inches",
                           fg = "white",
                           bg = "blue")
    self.lblInches.grid(row = 2, column = 0, sticky = "ew")
    self.txtInches = Entry(self.frame)
    self.txtInches.grid(row = 2, column = 1)
    self.txtInches.insert(INSERT, "0")
    
    self.btnCalc = Button(self.frame,
                          text = "Calculate BMI",
                          command = self.calc)
    self.btnCalc.grid(row = 3, column = 0, columnspan = 2)

    self.lblBMIPrompt = Label(self.frame,
                              text = "Body Mass Index",
                              fg = "white",
                              bg = "blue")
    self.lblBMIPrompt.grid(row = 4, column = 0, sticky = "ew")
    self.lblBMI = Label(self.frame, bg = "white", anchor = "w")
    self.lblBMI.grid(row = 4, column = 1, sticky = "ew")
    
    self.lblDescPrompt = Label(self.frame,
                               text = "Description",
                               fg = "white",
                               bg = "blue")
    self.lblDescPrompt.grid(row = 5, column = 0, sticky = "ew")
    self.lblDesc = Label(self.frame, bg = "white", anchor = "w")
    self.lblDesc.grid(row = 5, column = 1, sticky = "ew")
    
  def calc(self):    
    weight = float(self.txtWeight.get())
    feet = float(self.txtFeet.get())
    inches = float(self.txtInches.get())
    
    height = (feet * 12) + inches
    bmi = (weight * 703) / (height * height)
    self.lblBMI["text"] = "%.2f" % bmi
    
    desc = ""
    if bmi < 18.5:
      desc = "underweight"
    elif bmi < 25:
      desc = "normal"
    elif bmi < 30:
      desc = "overweight"
    else:
      desc = "obese"
      
    self.lblDesc["text"] = desc
    
def main():
  root = Tk()
  app = App(root)
  root.mainloop()
  
if __name__ == "__main__":
  main()

    