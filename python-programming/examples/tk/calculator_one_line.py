import tkinter as tk

app = tk.Tk()
app.title('Calculator')

entry = tk.Entry(app)
entry.pack()

def calc():
    print("clicked")
    inp = entry.get()
    print(inp)
    out = eval(inp)
    entry.delete(0, tk.END)
    entry.insert(0, out)

def close():
    app.destroy()
    exit()

calc_btn = tk.Button(app, text='Calculate', width=25, command=calc)
calc_btn.pack()


close_btn = tk.Button(app, text='Close', width=25, command=close)
close_btn.pack()

app.mainloop()
