# import tkinter library
from tkinter import *
#creating the window object
app = Tk()
x1 = IntVar()
x2 = IntVar()
color = {"x": "black"}
app.geometry('190x150')
#app.config(bg=color["black"])

#creating a variable x
x = Checkbutton(
    app,
    text="Checkbutton",
    variable=x1,
    onvalue=1,
    offvalue=0,
    height=5,
)
y = Checkbutton(
    app,
    text="Check",
    variable=x1,
    onvalue=1,
    offvalue=0,
    width=5,
    height=4,
)
z = Checkbutton(app,
                text="test",
                variable=x1,
                onvalue=1,
                offvalue=0,
                height=4,
                width=5,
                activebackground=color["x"])

x.pack()
y.pack()
z.pack()
#giving the window a new title
app.title("Checkbutton")
app.mainloop()