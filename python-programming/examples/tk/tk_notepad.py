import tkinter as tk

app = tk.Tk()
app.title('Menu')

def run_new():
    print("new")

def run_open():
    print("open")

def run_save():
    print("save")

def run_exit():
    print("exit")
    app.destroy()

def run_about():
    print("about")

menubar = tk.Menu(app)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="New",  underline=1, command=run_new)
menu1.add_command(label="Open", underline=1, command=run_open)
menu1.add_command(label="Save", underline=1, command=run_save)
menu1.add_separator()
menu1.add_command(label="Exit", underline=1, command=run_exit)
menubar.add_cascade(label="File", underline=0, menu=menu1)


menubar.add_command(label="About", command=run_about)

app.config(menu=menubar)

app.mainloop()

