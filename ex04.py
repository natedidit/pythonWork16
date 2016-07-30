from tkinter import *
from datetime import date

s = "Result: \n"

wd = date.today().weekday()
wd = int(wd)

switch = {
    0: "Today is Sunday \n\n",
    1: "Today is Monday\n\n",
    2: "Today is Tuesday\n\n",
    3: "Today is Wednesday\n\n",
    4: "Today is Thursday\n\n",
    5: "Today is Friday\n\n",
    6: "Today is Saturday\n\n"
}

s += str(switch[wd])

if wd == 0:
    s += str("Everything come to him who waits")
elif wd == 1:
    s += str("Give credit where credit is due")
elif wd == 2:
    s += str("If you pay peanuts, you get monkeys")
elif wd == 3:
    s += str("Money makes the world go round")
elif wd == 4:
    s += str("Prevention is better than cure")
elif wd == 5:
    s += str("Stupid is as stupid does")
else:
    s += str("The devil looks after his own")

# Message Box Code#######

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
