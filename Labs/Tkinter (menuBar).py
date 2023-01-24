import tkinter as tk
from tkinter import messagebox
def donothing():
    filewin=tk.Toplevel(root)
    button=tk.Button(filewin, text="Do nothing button")
    button.pack()
def a():
    filewin=tk.Toplevel(root)
    button=tk.Button(filewin, text="you have clicked open")
    button.pack()
def b():
    filewin=tk.Toplevel(root)
    button=tk.Button(filewin, text="you have clicked save")
    button.pack()

#lambda function defined 
def func(s):
    filewin=tk.Toplevel(root)
    button=tk.Button(filewin, text=s)
    button.pack()
    

root=tk.Tk()
menubar=tk.Menu(root)
#file menu details
filemenu=tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='New',command=donothing)
filemenu.add_command(label='Open',command=lambda:func("open")) #lambda func
filemenu.add_command(label='Save',command=b)
filemenu.add_command(label='Save as',command=donothing)
filemenu.add_command(label='Close',command=donothing)
menubar.add_cascade(label="file",menu=filemenu)
#edit menu details
editmenu=tk.Menu(menubar, tearoff=0)
editmenu.add_command(label='save',command=donothing)
editmenu.add_command(label='Open',command=donothing)
editmenu.add_command(label='Save',command=donothing)
editmenu.add_command(label='Save as',command=donothing)
editmenu.add_command(label='Close',command=donothing)
menubar.add_cascade(label="edit",menu=editmenu)
editmenu=tk.Menu(menubar, tearoff=0)
helpmenu=tk.Menu(menubar, tearoff=0)

root.config(menu=menubar)
root.mainloop()
