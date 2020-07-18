import tkinter as tk
from tkinter import ttk

countries = ["Japan", "Korea", "Vietnam", "China"]

app = tk.Tk()
app.title('Combo box')


def change(event):
    # VirtualEvent
    print("change")
    selection = country.current()
    print(selection)
    print(countries[selection])

def clicked():
    print("clicked")
    print(country.get())

country = ttk.Combobox(app, values=countries)
country.pack()
country.bind("<<ComboboxSelected>>", change)

button = tk.Button(app, text='Run', width=25, command=clicked)
button.pack()


app.mainloop()

