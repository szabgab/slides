import tkinter as tk

app = tk.Tk()
app.title('List box')


def clicked():
   print("clicked")
   selected = box.curselection()  # returns a tuple
   print(box.get(selected[0]))
   exit()

box = tk.Listbox(app)
box.insert(1, 'Red')
box.insert(2, 'Green')
box.insert(3, 'Blue')
box.insert(4, 'Purple')
box.pack()

button = tk.Button(app, text='Close', width=25, command=clicked)
button.pack()

app.mainloop()

