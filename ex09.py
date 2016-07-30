# Student: Nate Canney
# Programming Exercise: 09
from tkinter import *
import InputBox

s = ""

InputBox.ShowDialog("Enter your Student ID: ")
sid = InputBox.GetInput()
if not re.match(r"^D[0-9]{9}", sid):
    s += "Not a valid Student ID.\n"
else:
    s += "A valid a Student ID.\n"

InputBox.ShowDialog("Enter your CMS ID: ")
cmsid = InputBox.GetInput()
if not re.match(r"^@\d{9}s$", cmsid):
    s += "Not a valid CMS ID.\n"
else:
    s += "A valid CMS ID.\n"

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid()

root.mainloop()
