# this is all just code for the GUI. Actual code below.
from tkinter import *


# functions must be called first otherwise tkinter says they're not defined
def bmi_calc():
    prevresult=resultdisplay.get('1.0', END)
    if prevresult != '':
        resultdisplay.delete('1.0',END)
    weight = float(ew_value.get())
    height = float(eh_value.get())
    bmi = (weight / (height * height))
    new_weight = (height * height) * 20
    if 0 <= bmi <= 18:
        change = new_weight - weight
        cat = 'Underweight'
        lose_or_gain = "gain"
        resultdisplay.insert(END, "Your BMI is %s: \n%s\n" % (round(bmi, 2), cat))
        resultdisplay.insert(END, "You need to %s weight.\nThe amount of weight you need to %s is %skg." % (
        lose_or_gain, lose_or_gain, change))
    elif 19 <= bmi <= 24:
        cat = str("Your BMI is ") + str(round(bmi, 2)) + str("\nThis is a healthy weight for your height.")
        resultdisplay.insert(END, cat)
    elif 25 <= bmi <= 30:
        change = weight - new_weight
        lose_or_gain = "lose"
        cat = 'Overweight.'
        resultdisplay.insert(END, "Your BMI is %s: \n%s\n" % (round(bmi, 2), cat))
        resultdisplay.insert(END, "You need to %s weight.\nThe amount of weight you need to %s is %skg." % (
        lose_or_gain, lose_or_gain, change))
    elif 30 <= bmi <= 35:
        change = weight - new_weight
        lose_or_gain = "lose"
        cat = 'Obese Class I (Moderately obese)'
        resultdisplay.insert(END, "Your BMI is %s: \n%s\n" % (round(bmi, 2), cat))
        resultdisplay.insert(END, "You need to %s weight.\nThe amount of weight you need to %s is %skg." % (
        lose_or_gain, lose_or_gain, change))
    elif 35 <= bmi <= 1000:
        change = weight - new_weight
        lose_or_gain = "lose"
        cat = 'Obese Class II (Severely obese)'
        resultdisplay.insert(END, "Your BMI is %s: \n%s\n" % (round(bmi, 2), cat))
        resultdisplay.insert(END, "You need to %s weight.\nThe amount of weight you need to %s is %skg." % (
        lose_or_gain, lose_or_gain, change))

window = Tk()
window.title("BMI Calculator")
eh_label = Label(window, text="Enter your height in meters")
eh_label.grid(row=0, column=0)
eh_value = StringVar()
eh = Entry(window, textvariable=eh_value)
eh.grid(row=1, column=0)

ew_label = Label(window, text="Enter your weight in kg")
ew_label.grid(row=2, column=0)
ew_value = StringVar()
ew = Entry(window, textvariable=ew_value)
ew.grid(row=3, column=0)

resultdisplay = Text(window, height=10, width=45)
resultdisplay.grid(row=0, column=1, rowspan=4)

calc = Button(window, text="Calculate", height=3, width=30, command=bmi_calc)
calc.grid(row=4, column=0, columnspan=2)

window.mainloop()