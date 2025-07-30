import tkinter as tk

app = tk.Tk()
app.title('List box')


def clicked():
    print("clicked")
    selected = box.curselection()  # returns a tuple
    if selected:
        first = selected[0]
        color = box.get(first)
        print(color)

box = tk.Listbox(app)
values = ['Red', 'Green', 'Blue', 'Purple']
for val in values:
    box.insert(tk.END, val)
box.pack()

button = tk.Button(app, text='Show', width=25, command=clicked)
button.pack()

exit_button = tk.Button(app, text='Close', width=25, command=app.destroy)
exit_button.pack()

app.mainloop()
