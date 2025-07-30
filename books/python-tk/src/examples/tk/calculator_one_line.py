import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title('Calculator')

entry = tk.Entry(app)
entry.pack()

def calc():
    #print("clicked")
    inp = entry.get()
    print(f"'{inp}'")
    try:
        out = eval(inp)
    except Exception as err:
        messagebox.showwarning(title = "Error", message = f"Could not do the computation {err}")
        return
    entry.delete(0, tk.END)
    entry.insert(0, out)

def close():
    app.destroy()

calc_btn = tk.Button(app, text='Calculate', width=25, command=calc)
calc_btn.pack()


close_btn = tk.Button(app, text='Close', width=25, command=close)
close_btn.pack()

app.mainloop()
