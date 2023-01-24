from tkinter import *
import tkinter as tk

#defining the function
total = 0
def selection():
    global total
    number_of_hours = E1.get()
    type_of_vehicle = var.get()
    if type_of_vehicle == 1:
        amount = float(number_of_hours) * 100
    elif type_of_vehicle == 2:
        amount = float(number_of_hours) * 200
    text = f"Please collect rs. {amount}"
    L3 = tk.Label(win, text=text, bg='grey', font=('Arial', 15))
    L3.place(x=80,y=240)

    #displaying total amount
    total = total + amount
    ftext = f"Total collection: {total}"
    L4 = tk.Label(win, text=ftext, bg='grey', font=('Arial', 10))
    L4.place(x=350,y=280)
#creating an instance
win = tk.Tk()
win.geometry("500x300")
win.config(bg='grey')

Heading = tk.Label(win, text="Parking Fees Calculator", bg='grey', font=("Arial", 20))
L1 = tk.Label(win, text="Select Type of Vehicle: ", bg='grey',font=("Arial", 13))

var = IntVar()
R1 = Radiobutton(win, text="2 Wheeler", variable=var, value=1, bg='grey')
R2 = Radiobutton(win, text="4 Wheeler", variable=var, value=2, bg='grey')
L2 = tk.Label(win, text="Number of hours:", bg='grey', font=("Arial",13))
E1 = tk.Entry(win, bd=5)
Register = tk.Button(win, text="Calculate", command=lambda: selection(), bg='black', fg='white', pady=10, padx=80)

#defining placement of elements
Heading.place(x=80, y=20)
L1.place(x=30,y=80)
R1.place(x=230, y=80)
R2.place(x=330, y=80)
L2.place(x=30, y=120)
E1.place(x=250, y=120)
Register.place(x=150,y=170)

win.mainloop()
