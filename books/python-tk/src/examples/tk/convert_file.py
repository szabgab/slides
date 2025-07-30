import tkinter as tk
from tkinter import filedialog

def run_process():
    print("---- Start processing ----")
    title = title_entry.get()
    print(title)
    filename = input_file.get()
    print(filename)

    app.destroy()

def select_input_file():
    file_path = filedialog.askopenfilename()
    filedialog.asksaveasfile()
    print(file_path)
    input_file.set(file_path)

app = tk.Tk()
app.title('Convert file')

input_file = tk.StringVar()

title_label = tk.Label(app, text='Title')
title_label.pack()
title_entry = tk.Entry(app)
title_entry.pack()

input_button = tk.Button(app, text='Input file', command=select_input_file)
input_button.pack()
input_label = tk.Label(app, textvariable=input_file)
input_label.pack()


button = tk.Button(app, text='Process', width=25, command=run_process)
button.pack()

app.mainloop()


