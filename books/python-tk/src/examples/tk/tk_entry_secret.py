import tkinter as tk

app = tk.Tk()
app.title('Text Entry')

entry = tk.Entry(app)
entry['show'] = '*'
entry.pack()

def clicked():
    print(entry.get())

button = tk.Button(app, text='Show', width=25, command=clicked)
button.pack()

exit_button = tk.Button(app, text='Close', width=25, command=app.destroy)
exit_button.pack()

app.mainloop()

