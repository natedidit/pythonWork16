# Nate Canney
# Programming Exercise : 01
s = "T Swift is learning Python! "



####### Message Box Code#######
from tkinter import *
root = Tk()
root.title('Message Box')
Label (root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()