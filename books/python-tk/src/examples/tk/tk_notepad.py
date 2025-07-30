import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os

file_path = None

app = tk.Tk()
app.title('Tk Notepad')

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
    #print(dir(simpledialog))
    #answer = simpledialog.Dialog(app, "The title")
    messagebox.showinfo(title = "About", message = "This simple text editor was created as a solution for the exercise.\n\nCopyright: Gabor Szabo")

menubar = tk.Menu(app)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="New",  underline=0, command=run_new)
menu1.add_command(label="Open", underline=0, command=run_open)
menu1.add_command(label="Save", underline=0, command=run_save)
menu1.add_separator()
menu1.add_command(label="Exit", underline=1, command=run_exit)
menubar.add_cascade(label="File", underline=0, menu=menu1)

menubar.add_command(label="About", underline=0, command=run_about)

app.config(menu=menubar)

text = tk.Text(app)
text.pack({"side": "bottom"})

app.mainloop()

# TODO: Show the name of the file somewhere? Maybe at the bottom in a status bar?
# TODO: Indicate if the file has been changed since the last save?
# TODO: Ask before exiting or before replacing the content if the file has not been saved yet.
# TODO: Undo/Redo?
# TODO: Search?
# TODO: Search and Replace?

