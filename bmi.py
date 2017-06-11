from tkinter import *
class guicont:
    def __init__(self):
        self.window=Tk()
        self.window.title("BMI Calculator")
        self.window.mainloop()
    #
    # def buttons(self):
    #
    # def resultdisp(self):



class bmi_calc:
    def __init__(self, height, weight):
        self.weight = weight
        self.height = height

    def calculate(self):
        self.bmi = (self.weight / (self.height * self.height))
        return self.bmi

    def categorise(self):
        if 0 <= self.bmi <= 18:
            self.cat = 'Underweight'
            self.lose_or_gain = "gain"
            return self.cat
        elif 19 <= self.bmi <= 24:
            self.cat = 'Normal Weight'
            return self.cat
        elif 25 <= self.bmi <= 30:
            self.cat = 'Overweight'
            self.lose_or_gain = "lose"
            return self.cat
        elif 30 <= self.bmi <= 35:
            self.lose_or_gain = "lose"
            self.cat = 'Obese Class I (Moderately obese)'
            return self.cat
        elif 35 <= self.bmi <= 100000000:
            self.lose_or_gain = "lose"
            self.cat = 'Obese Class II (Severely obese)'
            return self.cat

    def newweight(self):
        new_weight = (self.height * self.height) * 20
        self.change = new_weight - self.weight
        self.newkg = str(self.change) + " Kg"
        return self.newkg

    def advice(self):
        print("Your BMI is %s: \n%s\n" % (round(self.bmi, 2), self.cat))
        print("You need to %s weight.\nThe amount of weight you need to %s is %s." % (self.lose_or_gain, self.lose_or_gain, self.newkg))


ben = bmi_calc(1.7, 3000) # TODO: try replacing with ew_value.get() etc
ben.calculate()
ben.categorise()
ben.newweight()
ben.advice()


# def bmi_calc():
#     prevresult=resultdisplay.get('1.0', END)
#     if prevresult != '':
#         resultdisplay.delete('1.0',END)
#     weight = float(ew_value.get())
#     height = float(eh_value.get())
#     bmi = (weight / (height * height))
#     new_weight = (height * height) * 20


#

    # if 0 <= bmi <= 18:
    #     change = new_weight - weight
    #     cat = 'Underweight'
    #     lose_or_gain = "gain"
    #     resultdisplay.insert(END, "Your BMI is %s: \n%s\n" % (round(bmi, 2), cat))
    #     resultdisplay.insert(END, "You need to %s weight.\nThe amount of weight you need to %s is %skg." % (
    #     lose_or_gain, lose_or_gain, change))
    # elif 19 <= bmi <= 24:
    #     cat = str("Your BMI is ") + str(round(bmi, 2)) + str("\nThis is a healthy weight for your height.")
    #     resultdisplay.insert(END, cat)
    # elif 25 <= bmi <= 30:
    #     change = weight - new_weight
    #     lose_or_gain = "lose"
    #     cat = 'Overweight.'
    #     resultdisplay.insert(END, "Your BMI is %s: \n%s\n" % (round(bmi, 2), cat))
    #     resultdisplay.insert(END, "You need to %s weight.\nThe amount of weight you need to %s is %skg." % (
    #     lose_or_gain, lose_or_gain, change))
    # elif 30 <= bmi <= 35:
    #     change = weight - new_weight
    #     lose_or_gain = "lose"
    #     cat = 'Obese Class I (Moderately obese)'
    #     resultdisplay.insert(END, "Your BMI is %s: \n%s\n" % (round(bmi, 2), cat))
    #     resultdisplay.insert(END, "You need to %s weight.\nThe amount of weight you need to %s is %skg." % (
    #     lose_or_gain, lose_or_gain, change))
    # elif 35 <= bmi <= 1000:
    #     change = weight - new_weight
    #     lose_or_gain = "lose"
    #     cat = 'Obese Class II (Severely obese)'
    #     resultdisplay.insert(END, "Your BMI is %s: \n%s\n" % (round(bmi, 2), cat))
    #     resultdisplay.insert(END, "You need to %s weight.\nThe amount of weight you need to %s is %skg." % (
    #     lose_or_gain, lose_or_gain, change))

# window = Tk()
# window.title("BMI Calculator")
# eh_label = Label(window, text="Enter your height in meters")
# eh_label.grid(row=0, column=0)
# eh_value = StringVar()
# eh = Entry(window, textvariable=eh_value)
# eh.grid(row=1, column=0)
#
# ew_label = Label(window, text="Enter your weight in kg")
# ew_label.grid(row=2, column=0)
# ew_value = StringVar()
# ew = Entry(window, textvariable=ew_value)
# ew.grid(row=3, column=0)
#
# resultdisplay = Text(window, height=10, width=45)
# resultdisplay.grid(row=0, column=1, rowspan=4)
#
# calc = Button(window, text="Calculate", height=3, width=30, command=bmi_calc)
# calc.grid(row=4, column=0, columnspan=2)
#
# window.mainloop()