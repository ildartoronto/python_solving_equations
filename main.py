from tkinter import *


root = Tk()
root.title("Solving Equations")

row1 = 3
borderW = 5


def addLabel(rowAfter, howMany):
    for i in range(1, howMany):        
        lab = Label(root, text=" ...              ").grid(row=rowAfter+i, column=0)


addLabel(0, 3)

myEntry1 = Entry(root, width=5, borderwidth=3)
myEntry1.grid(row=row1, column=0)
myEntry1.insert(0, "0")

myEntry2 = Entry(root, width=5, borderwidth=borderW).grid(row=row1, column=1)
myEntry3 = Entry(root, width=5, borderwidth=borderW).grid(row=row1, column=2)

myLabel1 = Label(root, text="=").grid(row=row1, column=3)

myEntry4 = Entry(root, width=5, borderwidth=borderW).grid(row=row1, column=4)
myEntry5 = Entry(root, width=5, borderwidth=borderW).grid(row=row1, column=5)
myEntry6 = Entry(root, width=5, borderwidth=borderW).grid(row=row1, column=6)

addLabel(3, 3)

def myClick(e):
    myLabelS.config(text="Solution: " + str(e))

myButton = Button(root, text="Solve!", padx=10, pady=10,
                  fg="white", bg="gray", command=lambda: myClick(5)).grid(row=5, column=3)

addLabel(5, 3)

myLabelS = Label(root, text="Solution: ")
myLabelS.grid(row=7, column=0)

addLabel(7, 3)

def calculate():
    pass


root.mainloop()
