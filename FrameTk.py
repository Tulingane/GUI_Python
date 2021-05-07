#Tkniter works like most of the python framworks in case to be used
# Let import the tkinter library

from tkinter import *
# Here I just create a window object
app = Tk()
f = Frame(app)
f.pack()
#let create a variable call label to label our frame
label = Label(f, text="Tkinter", fg="white")
label.pack()
# aligning the property right side and gives the text a skyblue color
btnA = Button(f, text="right", fg="skyblue")
btnA.pack(padx=5, pady=3, side=RIGHT)
#aligning the property left side and gives the text a darkgreen color
btnB = Button(f, text="left", foreground="darkgreen")
btnB.pack(
    padx=4,
    pady=5,
    side=LEFT,
)
#aligning the property on bottom and giving the text a blue color
btnA = Button(f, text="Bottom", fg="blue")
btnA.pack(padx=5, pady=3, side=BOTTOM)
#aligning the property top side and giving the text a darkgreen color
btnA = Button(f, text="TOP", fg="pink")
btnA.pack(padx=6, pady=4, side=TOP)
#giving the window a new title
app.title("This is my frame")
app.mainloop()
