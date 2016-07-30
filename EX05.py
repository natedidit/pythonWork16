import InputBox
from tkinter import *

s = ""
InputBox.ShowDialog("Enter your first name: ")
s1 = InputBox.GetInput()

for i in range(len(s1)-1, -1, -1):
    s += str((i+1) * s1[i]) + "\n"

# Message Box Code#######

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
