"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.title("Factoring Simple Trinomials")

foutput = StringVar()
foutput.set("Answer")

def clickFunction():
   m1= math.sqrt((b**2)-(4*a*c))
   m2= (-1*b)+m1
   x1=m2/(2*a)
   n1= math.sqrt((b**2)-(4*a*c))
   n2= (-1*b)-n1
   x2=n2/(2*a)
   lis=[]
   lis.append(x1)
   lis.append(x2)
   lis.sort()
   return lis

l1 = Label(win,title='fill in the coefficents for b and c.\nclick the "=" button and your factored equation will appear.\n *note: a is equal to 1*')
l2 = Label(win,title="")
l3 = Label(win,text="x^2")
l4 = Label(win,text="+")
e1 = Entry(win,width=5)
l5 = Label(win,text="x")
e2 = Entry(win,width=5)
l6 = Label(win,text="+")
b1 = Button(win,text="=",command=clickFunction)
f_entry = Entry(win,width=20,textvariable=foutput)



win.mainloop()