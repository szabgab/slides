import tkinter as tk
from tkinter import ttk


animals = ["Cow", "Elephant", "Snake", "Tiger"]

app = tk.Tk()
app.title('Combo box')


def change(event):
    # VirtualEvent
    print("change")
    selection = country.current()
    print(selection)
    print(animals[selection])

def clicked():
    print("clicked")
    print(country.get())

country = ttk.Combobox(app,  values=animals)
country.pack()
country.bind("<<ComboboxSelected>>", change)

button = tk.Button(app, text='Run', width=25, command=clicked)
button.pack()


app.mainloop()

