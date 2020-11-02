"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.title("madlib")

noutput = StringVar()
noutput.set("name")
thoutput = StringVar()
thoutput.set("theme")
poutput = StringVar()
poutput.set("a place")
doutput = StringVar()
doutput.set("day of the week")
toutput = StringVar()
toutput.set("time")
voutput = StringVar()
voutput.set("verb")
aoutput = StringVar()
aoutput.set("animal")
bpoutput = StringVar()
bpoutput.set("body part")
cioutput = StringVar()
cioutput.set("contact information")

def clickFunction():
    name = e1.get()
    theme = e2.get()
    place = e3.get()
    day = e4.get()
    time = e5.get()
    verb = e6.get()
    animal = e7.get()
    bodyp = e8.get()
    contacti = e9.get()

    n_entry.delete(0,END)
    n_entry.insert(0,name)
    th_entry.delete(0,END)
    th_entry.insert(0,theme)
    p_entry.delete(0,END)
    p_entry.insert(0,place)
    d_entry.delete(0,END)
    d_entry.insert(0,day)
    t_entry.delete(0,END)
    t_entry.insert(0,time)
    v_entry.delete(0,END)
    v_entry.insert(0,verb)
    a_entry.delete(0,END)
    a_entry.insert(0,animal)
    bp_entry.delete(0,END)
    bp_entry.insert(0,bodyp)
    ci_entry.delete(0,END)
    ci_entry.insert(0,contacti)

l1 = Label(win,text="name:")
e1 = Entry(win, width=15)
l2 = Label(win,text="theme:")
e2 = Entry(win, width=15)
l3 = Label(win,text="a place:")
e3 = Entry(win, width=15)
l4 = Label(win,text="day of the week:")
e4 = Entry(win, width=15)
l5 = Label(win,text="time:")
e5 = Entry(win, width=15)
l6 = Label(win,text="verb:")
e6 = Entry(win, width=15)
l7 = Label(win,text="animal")
e7 = Entry(win, width=15)
l8 = Label(win,text="body part:")
e8 = Entry(win, width=15)
l9 = Label(win,text="contact information:")
e9 = Entry(win, width=15)

b1 = Button(win,text="Update madlib", command=clickFunction)

l10 = Label(win,text="is having a")
l12 = Label(win,text="party!")
l13 = Label(win,text="It's going to be at")
l14 = Label(win,text="on")
l15 = Label(win,text="Please make sure to show up at")
l16 = Label(win,text=", or else")
l17 = Label(win,text="you will be required to")
l18 = Label(win,text="a/an")
l19 = Label(win,text="with your")
l20 = Label(win,text="RSVP at")

n_entry = Entry(win, width=15, textvariable=noutput)
th_entry = Entry(win, width=15, textvariable=thoutput)
p_entry = Entry(win, width=15, textvariable=poutput)
d_entry = Entry(win, width=15, textvariable=doutput)
t_entry = Entry(win, width=15, textvariable=toutput)
v_entry = Entry(win, width=15, textvariable=voutput)
a_entry = Entry(win, width=15, textvariable=aoutput)
bp_entry = Entry(win, width=15, textvariable=bpoutput)
ci_entry = Entry(win, width=15, textvariable=cioutput)

l1.grid(row= ,column= )
e1.grid(row= ,column= )
l2.grid(row= ,column= )
e2.grid(row= ,column= )
l3.grid(row= ,column= )
e3.grid(row= ,column= )
l4.grid(row= ,column= )
e4.grid(row= ,column= )
l5.grid(row= ,column= )
e5.grid(row= ,column= )
l6.grid(row= ,column= )
e6.grid(row= ,column= )
l7.grid(row= ,column= )
e7.grid(row= ,column= )
l8.grid(row= ,column= )
e8.grid(row= ,column= )
l9.grid(row= ,column= )
e9.grid(row= ,column= )




win.mainloop()