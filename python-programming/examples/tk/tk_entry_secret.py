import tkinter as tk

app = tk.Tk()
app.title('Text Entry')

entry = tk.Entry(app)
entry['show'] = '*'
entry.pack()

def clicked():
    print("clicked")
    print(entry.get())
    app.destroy()
    exit()

button = tk.Button(app, text='Close', width=25, command=clicked)
button.pack()
app.mainloop()

