#Graphic User Interface in Python
# Intro
#A GUI is a computer human interface on a computer
#GUI are trying to solve the blank screen problem and cover the algorithm and code behind any program
#Python has a numerous GUI frameworks let start with the most used which is Tkinter
#Let try to run this command and see the output
#python -m tkinter
#when running the code it's brint the screen with title tkinter and asking to be clicked
# Tkniter works like most of the python framworks in case to be used
# we've to be imported and then we can use
#let create a simple output with
from tkinter import *
from db import Database

db = Database('store.db')


# We create a function to pop the list buttons to make
# sure our buttons when clicked they should respond
#the function populate list help to show up the itmes in the list
#We're going to fetch the data using fetch
def populate_list():
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    print('Add')


def remove_item():
    print('Remove')


def update_item():
    print('Update')


def clear_text():
    print('Clear')


# Create a window object
app = Tk()
add_item = 0

#giving the window a new title
# let create the lables
#let create a variable call part
part_text = StringVar()  # pady for spacing
part_label = Label(app, text='Part name', font=('bold', 14), pady=20)
#trying to align the property left or east using sticky = w(west)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

#let create a variable call customer
customer_text = StringVar()  # pady for spacing
customer_label = Label(app, text='Customer name', font=('bold', 14))
#trying to align the property left or east using sticky = w(west)
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=part_text)
customer_entry.grid(row=0, column=3)

#let create a variable call Retailer
retailer_text = StringVar()  # pady for spacing
retailer_label = Label(app, text='Retailer name', font=('bold', 14))
#trying to align the property left or east using sticky = w(west)
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=part_text)
retailer_entry.grid(row=1, column=1)

#let create a variable call Price
price_text = StringVar()  # pady for spacing
price_label = Label(app, text='Price', font=('bold', 14))
#trying to align the property left or east using sticky = w(west)
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=part_text)
price_entry.grid(row=1, column=3)

#Parts list (listbox)
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
#Let create a scrollbar it will show up but it wan't be connected to any table yet
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
#Setting scrollbar to the listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

#Adding buttons
add_btn = Button(app, text='Add part', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='remove part', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update part', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

app.title('Part Manager')
#to give the window a certain size we're using a method call geometry
app.geometry('600x500')

# Populate data to populate the list
populate_list()

# Start running the program
app.mainloop()