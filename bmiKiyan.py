#Kiyan Allaei
#BMI assignment

from Tkinter import *

#create a Tk class
class app(Tk):
    #define initial function
    def __init__(self):
        #__init__ was misspelled __intit__
        Tk.__init__(self)
        
        #make the header helvetics with 16 font size, bold, and italic
        self.headerFont = ("Helvetica", "16", "bold italic")
        #make the title "Body Mass Index Calculator"
        self.title("Body Mass Index Calculator")
        
        #call the inner functions 
        self.bmiIndex()
	#it doesn't make sense to calculate the BMI until
	#the user has entered data
	#self.calcBMI()
        
    def bmiIndex(self):
        #Make a label to show that the need for weight in pounds at the top
        Label(self, text = "Weight (In pounds):").grid(row = 0, column = 0)
        #make a label for height in feet under the previous label
        Label(self, text = "Feet:").grid(row = 1, column = 0)
        #make a label for height in inches under the previous label
        Label(self, text = "Inches:").grid(row = 2, column = 0)
        #make a label for the bmi
        Label(self, text = "Your body mass index is: ").grid(row = 5, column = 0)
        #make a label saying if they are underweight, normal, overweight or obese
        Label(self, text = "You are: ").grid(row = 4, column = 0)

        #make a label that shows what their BMI is
        #we don't know what the BMI is yet, because they've not
        #entered any data
        #This label will be called later in code, so it needs an explicit name
        #Label(self, text = "%.2f" % BMI).grid(row = 5, column = 1)
        self.lblBmi = Label(self)
	self.lblBmi.grid(row = 5, column = 1)
        
        #make a label showing if they are underweight, normal, overweight or obese
	#this will likewise need a name, because we don't know its value yet
        self.lblStatus = Label(self)
	self.lblStatus.grid(row = 6, column = 1)
        
        #make the entry for the entry box next to the weight label the weight value
        self.weightInput = Entry(self)
        self.weightInput.grid(row = 0, column = 1)
        
        #make the entry for the entry box next to the height in feet label the feet value
        self.feetInput = Entry(self)
        self.feetInput.grid(row = 1, column = 1)
        
        #make the entry for the entry box next to the height in inches label the inches value
        self.inchesInput = Entry(self)
        self.inchesInput.grid(row = 2, column = 1)
        
        #make a button that says calculate under the labels and inbetween the labels and boxes
        self.BMIbtn = Button(self, text = "Calculate")
	self.BMIbtn.grid(row = 5, column = 5)
	self.BMIbtn["command"] = self.calcBMI
        
    
    #make a function for calculating the BMI
    def calcBMI(self):
        #get the value for weight
        weight = int(self.weightInput.get())
        #get the value for feet
        feet = int(self.feetInput.get())
        #get the value for inches
        inches = int(self.inchesInput.get())
        #use the feet, weight, and inches values in the BMI formula to calculate it
        BMI = (weight * 703) / (feet * 12 + inches)
	#is BMI the numeric value or the status?  It can't be both.
	#you need another variable
        if BMI < 18.5:
            BMI = "Underweight."
        elif 18.51 < BMI < 24.9:
            BMI = "Normal."
        elif 25 < BMI < 29.9:
            BMI = "Overweight."
        elif 30 < BMI:
            BMI = "Obese."
        #program the button
	
	#this doesn't go here, but in initialization
        #BMIbtn["command"] = self.calculate
	
	"""I've given you a lot of help.  Now figure out how to
	   map the calculated BMI and status back to the GUI.
	"""
        
#define the main function with a main loop
def main():
    App = app()
    App.mainloop()

#call the main function
if __name__ == "__main__":
    main()

