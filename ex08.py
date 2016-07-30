# Student: Nate Canney
# Programming Exercise: 08

import InputBox
import MessageBox


def reverseit(s):
    s1 = s
    s2 = ""
    for i in range(len(s1)-1, -1, -1):
        s2 = s2 + s1[i] + " "
    for i in range(len(s1)-1, -1, -1):
        if i % 10 == 0:
            s2 = s2 + s1[i] + "\n"
    return s2


def main():

    InputBox.ShowDialog("Enter a paragraph: ")
    s = InputBox.GetInput()
    s = s.split(" ")

    result = reverseit(s) + "\n"

    MessageBox.Show(result)

if __name__ == "__main__":
    main()



'''TAIPEI 101, formerly known as the Taipei World
Financial Center, is a landmark supertall skyscraper in
Xinyi District, Taipei, Taiwan. The building was
officially classified as the world's tallest in 2004.'''

