# Student: Nate Canney
# Programming Exercise: 12
import string
import math
import InputBox
from tkinter import *


def getsqrt(n):
    return math.sqrt(float(n))

InputBox.ShowDialog("Enter a hexadecimal value: ")
while True:
    try:
        n = InputBox.GetInput()
        n = int(n, 16)
        break
    except ValueError:
        raise ValueError("Non Numerical value")
s = str(getsqrt(n)) + "\n"

root = Tk()

root.title('Message Box')
Label(root, justify=LEFT, text=s).grid()

root.mainloop()
