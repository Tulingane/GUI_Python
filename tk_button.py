#Always remember to import tkinter library
from tkinter import *
# Here I just create a window object
app = Tk()
f = Frame(app)
f.pack()


# creating a function just to pop up a button message
def test():
    print('Button')


#aligning the property on bottom and giving the text a blue color
btnA = Button(f, text="Button A", fg="red")
btnA.pack(padx=4, pady=3)

btnA = Button(f, text="Button B ", fg="white")
btnA.pack(padx=4, pady=3)

btnA = Button(f, text="Button C", fg="black", command=test)
btnA.pack(padx=4, pady=3)

#giving the window a new title
app.title("This are my buttons")
app.mainloop()