import tkinter as tk

app = tk.Tk()
app.title('Checkbox')

var1 = tk.IntVar()
cb1 = tk.Checkbutton(app, text='male', variable=var1)
cb1.pack()

var2 = tk.IntVar()
cb2 = tk.Checkbutton(app, text='female', variable=var2)
cb2.pack()

def clicked():
   print(var1.get())
   print(var2.get())
   exit()

button = tk.Button(app, text='Close', width=25, command=clicked)
button.pack()
app.mainloop()

