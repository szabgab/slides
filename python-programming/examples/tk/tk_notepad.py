import tkinter as tk
from tkinter import filedialog
import os

file_path = None

app = tk.Tk()
app.title('Menu')

def run_new():
    global file_path
    file_path = None
    text.delete(1.0, tk.END)

def run_open():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=(("Any file", "*"),))
    if file_path and os.path.isfile(file_path):
        with open(file_path) as fh:
            content = fh.read()
        text.delete(1.0, tk.END)
        text.insert('end', content)

def run_save():
    global file_path
    if file_path is None:
        file_path = filedialog.asksaveasfilename(filetypes=(("Any file", "*"),))
        if not file_path:
            file_path = None
            return
    #print(f"'{file_path}'")
    content = text.get(1.0, tk.END)
    with open(file_path, 'w') as fh:
        fh.write(content)

def run_exit():
    print("exit")
    app.destroy()

def run_about():
    print("about")

menubar = tk.Menu(app)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="New",  underline=0, command=run_new)
menu1.add_command(label="Open", underline=0, command=run_open)
menu1.add_command(label="Save", underline=0, command=run_save)
menu1.add_separator()
menu1.add_command(label="Exit", underline=1, command=run_exit)
menubar.add_cascade(label="File", underline=0, menu=menu1)

menubar.add_command(label="About", command=run_about)

app.config(menu=menubar)

text = tk.Text(app)
text.pack({"side": "bottom"})

app.mainloop()

