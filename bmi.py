# this is all just code for the GUI. Actual code below.
from tkinter import *


# functions must be called first otherwise tkinter says they're not defined
def bmi_calc():
    weight = float(ew_value.get())
    height = float(eh_value.get())
    bmi = (weight / (height * height))
    new_weight = (height * height) * 20
    change = ''
    lose_or_gain = ''
    if 0 <= bmi <= 18:
        change = new_weight - weight
        cat = 'Underweight'
        lose_or_gain = "gain"
        resultdisplay.insert(END, "Your BMI is %s. \n%s\n" % (round(bmi, 2), cat))
        resultdisplay.insert(END, "You need to %s weight. The weight you need to %s is %skg." % (
        lose_or_gain, lose_or_gain, change))
    elif 19 <= bmi <= 24:
        lose_or_gain = "lose"
        cat = str("Your BMI is ") + str(round(bmi, 2)) + str(" This is a healthy weight for your height.")
        resultdisplay.insert(END, cat)
    elif 25 <= bmi <= 30:
        change = weight - new_weight
        lose_or_gain = "lose"
        cat = 'Overweight.'
        resultdisplay.insert(END, "Your BMI is %s. \n%s\n" % (round(bmi, 2), cat))
        resultdisplay.insert(END, "You need to %s weight. The weight you need to %s is %skg." % (
        lose_or_gain, lose_or_gain, change))
    elif 30 <= bmi <= 35:
        change = weight - new_weight
        lose_or_gain = "lose"
        cat = 'Obese Class I (Moderately obese)'
        resultdisplay.insert(END, "Your BMI is %s. \n%s\n" % (round(bmi, 2), cat))
        resultdisplay.insert(END, "You need to %s weight. The weight you need to %s is %skg." % (
        lose_or_gain, lose_or_gain, change))
    elif 35 <= bmi <= 1000:
        change = weight - new_weight
        lose_or_gain = "lose"
        cat = 'Obese Class II (Severely obese)'
        resultdisplay.insert(END, "Your BMI is %s. \n%s\n" % (round(bmi, 2), cat))
        resultdisplay.insert(END, "You need to %s weight. The weight you need to %s is %skg." % (
        lose_or_gain, lose_or_gain, change))


# new_weight_func works out how much you need to gain or lose to be right bmi
# def new_weight_func(height, weight):
#     bmi = (weight / (height * height))
#     new_weight = (height * height) * 20
#     change = ''
#     lose_or_gain = ''
#     if 0 <= bmi <= 18:
#         change = new_weight - weight
#         lose_or_gain = "gain"
#         print("You need to %s weight. The weight you need to %s is %skg." % (lose_or_gain, lose_or_gain, change))
#     elif 25 <= bmi <= 1000000000:
#         change = weight - new_weight
#         lose_or_gain = "lose"
#         print("You need to %s weight. The weight you need to %s is %skg." % (lose_or_gain, lose_or_gain, change))
#

# the capital below is SUPER important - won't work unless "Tk"
window = Tk()
calc = Button(window, text="Calculate", height=3, width=30, command=bmi_calc)
# there are 5 rows, counting from 0: 2 pairs of text box + button, and the Calculate button
# 2 columns, inputs on one side, outputs on the other
# we're starting from the bottom because I am a difficult person
# you can also use rowspan=1 (or 2, 3 etc) to make the thing span multiple rows
calc.grid(row=5, column=1, rowspan=2, columnspan=2)
# eh = Enter Height - this is a text input box
eh_value = StringVar()
eh = Entry(window, textvariable=eh_value)
eh.grid(row=0, column=1)

ew_value = StringVar()
ew = Entry(window, textvariable=ew_value)
ew.grid(row=3, column=1)

# righto then, now we need the 2 display windows on the right:
# one for general bmi info above, and the result displayed below
# dunno what the height/width units are so have a guess
bmiinfo = Text(window, height=10, width=30)
bmiinfo.grid(row=0, column=2, rowspan=1)

resultdisplay = Text(window, height=10, width=30)
resultdisplay.grid(row=3, column=2, rowspan=2)

# print("BMI Calculator version 3, now in Python 3")
# height = float(input("What is your height in meters?\n"))
# weight = float(input("What is your weight in kilograms?\n"))
# bmi_calc(height, weight)
# new_weight_func(height, weight)

# this is VERY IMPORTANT: delays ending the loop. otherwise it'd just open then close
window.mainloop()
