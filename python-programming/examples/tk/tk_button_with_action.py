import tkinter as tk

def clicked():
   print("clicked")
   exit()

app = tk.Tk()
app.title('Single Button')
button = tk.Button(app, text='Close', width=25, command=clicked)
button.pack()
app.mainloop()

