# Student: Nate Canney
# Programming Exercise: 03

import InputBox
import MessageBox

import InputBox
InputBox.ShowDialog("Enter the atomic mass of silicon in grams:")
f = InputBox.GetInput()
w = (float(f) / 28.09 * (6.022*(10**23)))


import MessageBox
MessageBox.Show("This sample has" + " " + (str(w)) + " " + "of silicon atoms")