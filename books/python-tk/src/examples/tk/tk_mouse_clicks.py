import tkinter as tk

app = tk.Tk()
app.title('Key binding')

label = tk.Label(app, text='Click the buttons of the mouse on the window')
label.config(font=("Courier", 44))
label.pack()

def action(event):
    print(dir(event))
    print(event.num)
    print(event.type)
    print(event.x)
    print(event.y)
    print()

app.bind("<ButtonPress-1>", action)
app.bind("<ButtonPress-2>", action)
app.bind("<ButtonPress-3>", action)
app.bind("<ButtonRelease-1>", action)
app.bind("<ButtonRelease-2>", action)
app.bind("<ButtonRelease-3>", action)

app.mainloop()
