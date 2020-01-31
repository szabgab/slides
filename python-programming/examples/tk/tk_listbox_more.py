import tkinter as tk

app = tk.Tk()
app.title('List box')


def clicked():
   print("clicked")
   selected = box.curselection()  # returns a tuple
   for idx in selected:
       print(box.get(idx))
   exit()

box = tk.Listbox(app, selectmode=tk.MULTIPLE, height=4)
values = ['Red', 'Green', 'Blue', 'Purple', 'Yellow', 'Orange', 'Black', 'White']
for val in values:
   box.insert(tk.END, val)
box.pack()

button = tk.Button(app, text='Close', width=25, command=clicked)
button.pack()

app.mainloop()


