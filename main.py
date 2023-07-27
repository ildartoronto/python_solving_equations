from tkinter import *

row1 = 3
borderW = 3
# bg = "gray"
bg = "#999999"

root = Tk()
root.title("Solving Equations")
root.configure(bg=bg)

def createLabel(text, row, column, fg='blue'):
    Label(root, text=text, font="Helvetica 44 bold",
          fg=fg, bg=bg).grid(row=row, column=column)


def createEntry(row, column):
    e = Entry(root, width=5, borderwidth=borderW,
              font="Helvetica 44 bold", justify='center', bg="yellow")
    e.grid(row=row, column=column)
    return e


Label(root, text="     ", bg=bg).grid(row=0, column=0)
Label(root, text="     ", bg=bg).grid(row=1, column=0)

# ------------------------------ left side ------------------------------
e1 = createEntry(row1, 1)
e1.insert(0, "x6")

createLabel("+", row1, 2)

e2 = createEntry(row1, 3)
e2.insert(0, "-20")

createLabel("+", row1, 4)

e3 = createEntry(row1, 5)
e3.insert(0, "x7")
# ------------------------------ left side end ------------------------------

createLabel("=", row1, 6, 'red')

# ------------------------------ right side ------------------------------
e4 = createEntry(row1, 7)
e4.insert(0, "10")

createLabel("+", row1, 8)

e5 = createEntry(row1, 9)
e5.insert(0, "-50")

createLabel("+", row1, 10)

e6 = createEntry(row1, 11)
e6.insert(0, "-x4")
# ------------------------------ right side end ------------------------------


Label(root, text='     ', bg=bg).grid(row=row1, column=12)

xs = 0
numbers = 0


def addNumbers(strNumber, sign=1):
    global numbers
    if strNumber == "":
        return
    isFindX = strNumber.find("x")
    # if there is no "x" in strNumber
    if isFindX == -1:
        numbers = numbers + int(strNumber) * sign
        # print("adding ", int(strNumber) * sign)


def addXs(x_element, sign=""):
    global xs
    if x_element == "":
        return
    isFindX = x_element.find("x")
    if isFindX != -1:   # if there is "x" in x_element
        x_2_add = ""
        if sign == "-":
            # if there is minus in x, i.e. -4x, remove it
            isFindMinus = x_element.find("-")
            if isFindMinus != -1:
                x_2_add = x_element.replace("-", "")
            else:
                x_2_add = sign+x_element
        else:
            x_2_add = x_element

        x_2_add = x_2_add.replace("x", "")
        if x_2_add == "":
            x_2_add = "1"
        elif x_2_add == "-":
            x_2_add = "-1"
        xs = xs + int(x_2_add)

        # print("adding ", x_2_add, ' to xs array')


def addAllXs():
    addXs(e1.get())
    addXs(e2.get())
    addXs(e3.get())
    addXs(e4.get(), "-")
    addXs(e5.get(), "-")
    addXs(e6.get(), "-")


def addAllNumbers():
    addNumbers(e1.get(), -1)
    addNumbers(e2.get(), -1)
    addNumbers(e3.get(), -1)
    addNumbers(e4.get())
    addNumbers(e5.get())
    addNumbers(e6.get())


def findSolution():
    global xs
    global numbers
    xs = 0
    numbers = 0

    addAllXs()
    addAllNumbers()

    # print("xs: ", xs)
    # print("numbers: ", numbers)

    solution = str(numbers/xs)
    myLabelS.config(text="x = " + solution)


Label(root, text="     ", bg=bg).grid(row=row1+1, column=0)
Label(root, text="     ", bg=bg).grid(row=row1+2, column=0)

solveButton = Button(root, text="Solve", padx=100, pady=10, font="Helvetica 42 bold",
                     fg="white", bg="gray", command=findSolution)
solveButton.grid(row=6, column=1, columnspan=12)

Label(root, bg=bg).grid(row=7, column=0)
Label(root, bg=bg).grid(row=8, column=0)

myLabelS = Label(root, text="Click the button above to solve!",
                 font="Helvetica 32 bold", fg="green", bg=bg)
myLabelS.grid(row=9, column=1, columnspan=12)

Label(root, bg=bg).grid(row=10, column=0)
Label(root, bg=bg).grid(row=11, column=0)



def calculate():
    pass


root.mainloop()
