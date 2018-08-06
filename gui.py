import tkinter as tk
from tkinter import *
window = tk()

l1=Label(window,text='User:')
l2=Label(window,text='Password')

t1=Entry(window,textvariable=StringVar())
t2=Entry(window,textvariable=StringVar())

b1=Button(window,text="LOG_IN")

l1.pack()
t1.pack()
l2.pack()
t2.pack()
b1.pack()

window.mainloop()

