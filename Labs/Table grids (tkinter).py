import tkinter as tk
class Table:
    #initialize a constructor
    def __init__(self, gui):
        for i in range(total_rows):
            for j in range(total_columns):
                #print(i)
                if i==0:
                    self.entry=tk.Entry(gui, width=10, bg='LightSteelBlue', fg='Black',
                                     font=('Arial', 16, 'bold'))
                else:
                    self.entry=tk.Entry(gui, width=10, fg='blue',
                                     font=('Arial', 16, ''))
                    self.entry.grid(row=i, column=j, padx=7, pady=1) # padx pady for gaps
                    self.entry.insert(tk.END, employee_list[i][j])
                    self.entry.grid(row=1, column =j, padx=7, pady=1)
                    self.entry.insert(tk.END, employee_list[i]+[j])



#take the data
employee_list=[('reg no', 'name', 'course1', 'course2'),
                             (111, 'ram', 21, 21),
                             (222, 'sumit', 78, 34),
                             (333, 'honey', 34, 33),
                             (444, 'badshah', 54, 33),
                             (555, 'sunil', 47, 31),
                             (666, 'krishna', 67, 64)]
#find total number of rows
total_rows=len(employee_list)
total_columns=len(employee_list[0])
# create root window
gui=tk.Tk()
table=Table(gui)
gui.mainloop()

