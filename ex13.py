# Student: Nate Canney
# Programming Exercise: 13

import tkinter


def resize():
    x = root.winfo_width() * 1.5
    y = root.winfo_height() * 1.5
    root.geometry("%dx%d+0+0" % (x, y))


root = tkinter.Tk()

window = tkinter.Button(root, text=' Resize ', command=resize)
window.pack()

root.mainloop()
