# Student: Nate Canney
# Programming Exercise: 11
from tkinter import *
s = ""


class division:
    dt = ""
    ft = 0
    pt = 0

    def getlist(self):
        dt = self.dt
        ft = self.ft
        pt = self.pt
        return "The " + dt + " department has " + str(ft) + " full-time and " + str(pt) + \
               " part-time instructors."


class department(division):
    dt = "CIS "
    ft = 12
    pt = 27

    def __init__(self):
        self.dt
        self.ft
        self.pt

mydiv = division()
mydiv.ft = 0
mydiv.pt = 0
mydept = department()
mydept.ft = 12
mydept.pt = 27
mydept.dt = "CIS "

s += str(type(mydiv)) + "\n"
s += mydiv.__class__.__name__ + "\n"
s += str(mydiv.getlist()) + "\n\n"
s += str(type(mydept)) + "\n"
s += mydept.__class__.__name__ + "\n"
s += str(mydept.getlist()) + "\n\n"


root = Tk()

root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
