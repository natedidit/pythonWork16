# Student: Nate Canney
# Programming Exercise: 07


def pv(fv, r, n):
    r = r/100
    return fv / ((1+r)**n)


def main():

    import InputBox
    InputBox.ShowDialog("Enter the future value: ")
    fv = float(InputBox.GetInput())

    InputBox.ShowDialog("Enter the interest rate: ")
    r = float(InputBox.GetInput())

    InputBox.ShowDialog("Enter the number of years: ")
    n = int(InputBox.GetInput())

    present = pv(fv, r, n)

    s = "Present Value: " + '${:,.2f}'.format(present) + "\n"

    import MessageBox
    MessageBox.Show(s)

if __name__ == "__main__":
    main()
