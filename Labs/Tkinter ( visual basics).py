import tkinter as tk
def display_text():
    global entry
    string = entry.get()
    finalString="welcome," +string
    output.configure(text=finalString)
    
window = tk.Tk()
window.geometry('300x200')
window.configure(bg = "white")
label = tk.Label(text='Name')
entry = tk.Entry()
button=tk.Button(
    text="click me!",
    width = 25,
    height = 5,
    bg = 'blue',
    fg = 'yellow',
    command = display_text,
    )
label.pack(pady=250)
entry.pack(pady=10)
button.pack(pady=10)
output.pack(pady=10)
name = entry.get(pady=10)

print(name)
name = entry.get()
window.mainloop()
