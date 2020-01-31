import tkinter as tk

# This solutions is not ready yet

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

def enter(num):
    entry.insert(tk.END, num)

def add_button(num):
    btn = tk.Button(app, text=num, width=25, command=lambda : enter(num))
    btn.pack()
    buttons[num] = btn

buttons = {}
for num in range(10):
    add_button(num)
for op in ['+', '-', '*', '/']
    add_button(op)


calc_btn = tk.Button(app, text='Calculate', width=25, command=calc)
calc_btn.pack()


close_btn = tk.Button(app, text='Close', width=25, command=close)
close_btn.pack()

app.mainloop()
