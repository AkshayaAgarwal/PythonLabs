#selection of favourite course  
import tkinter as tk
win=tk.Tk()
win.geometry("700x350")
def selection():
    val=str(radio.get())
    course=["dlf", "stats", "OS", "PYTHON", "C"]
    selected = "Your Favourite course is " + course[int(val)]
    label.config(text=selected)

tk.Label(text="Select your favourite course in MCA", font=('Aerial 11')).pack()
radio=tk.IntVar(win)

r1=tk.Radiobutton(win, text="DLF",  variable=radio,
                  value=0, command=selection).pack()
r2=tk.Radiobutton(win, text="STATS",  variable=radio,
                  value=1, command=selection).pack()
r3=tk.Radiobutton(win, text="OS",  variable=radio,
                  value=2, command=selection).pack()
r4=tk.Radiobutton(win, text="PYTHON",  variable=radio,
                  value=3, command=selection).pack()
r5=tk.Radiobutton(win, text="C",  variable=radio,
                  value=4, command=selection).pack()
label=tk.Label(win)
label.pack()

win.mainloop()
