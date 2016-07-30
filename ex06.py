# Student: Nate Canney
# Programming Exercise: 06

from tkinter import *

weekday = ["Monday", "Tuesday",
           "Wednesday", "Thursday", "Friday",
           "Saturday", "Sunday"]
weekday[0] = "day 1: Monday" + "\n"
weekday[1] = "day 2: Tuesday" + "\n"
weekday[2] = "day 3: Wednesday" + "\n"
weekday[3] = "day 4: Thursday" + "\n"
weekday[4] = "day 5: Friday" + "\n"
weekday[5] = "day 6: Saturday" + "\n"
weekday[6] = "day 7: Sunday" + "\n"

s = weekday

# Message Box Code#######

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
