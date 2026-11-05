from tkinter import *
from datetime import date

root = Tk()
root.title('Getting started with Widgets')
root.geometry('400x300')


lbl = Label(text="Hey THere!" ,fg="white",bg="#072f5f",height=1,width=300)
name_lbl = Label(text="Full Name", bg="#3895d3")
name_entry = Entry()

text_box = Text(height=3)

def display():
    name = name_entry.get()
    global message
    message = "WElcome to the Application! \nToday's date is: "
    greet = "Hello"+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

my_button = Button(text="Begin",command=display,height=1, bg="#1261A0", fg='white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
my_button.pack()
text_box.pack()

root.mainloop()