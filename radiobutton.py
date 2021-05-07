#Always remember to import tkinter library

from tkinter import *

app = Tk()
app.geometry("500x250")
#Setting the dictionary of color
color = {"b": "black", "g": "purple"}
# Setting root window
app.title("RadioButton")

# Variable of a radio button
x = IntVar()

#set y coordinate for the loop
y = 20
# Radiobutton set1
for i in range(3):
    Radiobutton(app,
                text="Button" + str(i + 1),
                bg=color["g"],
                selectcolor=color["b"],
                activebackground=color["b"],
                value=i + 1,
                var=x).place(x=100, y=y)
    y += 50

btnA = Radiobutton(app, text="Button", fg="white", activebackground=color["b"])
btnA.pack(padx=15, pady=13)
# app in mainloop

app.mainloop()