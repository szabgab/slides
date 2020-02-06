import tkinter as tk

app = tk.Tk()
app.title('Checkbox')

var1 = tk.BooleanVar()
cb1 = tk.Checkbutton(app, text='male', variable=var1)
cb1.pack()

var2 = tk.BooleanVar()
cb2 = tk.Checkbutton(app, text='female', variable=var2)
cb2.pack()

def clicked():
    print(var1.get())
    print(var2.get())

button = tk.Button(app, text='Show', width=25, command=clicked)
button.pack()

exit_button = tk.Button(app, text='Close', width=25, command=app.destroy)
exit_button.pack()

app.mainloop()

