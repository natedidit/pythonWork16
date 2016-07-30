# Student: Nate Canney
# Programming Exercise: 09

import MessageBox
import os


def main():
    result = ""
    if not os.path.exists('Elite01'):
        result = "elite01 does not exist \n"
        os.mkdir("Elite01")
        result += "just created elite01 \n"
        f = open('Elite01\message.txt', 'w+')
        f.write("I used python to create this file")
        f.close()
        result += "The message.txt file was also created \n\n\n"

    else:
        result = "elite01 exists. The message.txt file contains...\n"
        f = open('Elite01\message.txt', 'r')
        for line in f:
            result += line + "\n\n\n"
        f.close()

    result += "elite01 contains:\n"
    result += str(os.listdir('Elite01'))

    MessageBox.Show(result)

if __name__ == "__main__":
    main()


