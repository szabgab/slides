import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title('Single Button')

progressbar = ttk.Progressbar(app)
progressbar.pack()

def stop():
    progressbar.stop()

def start():
    app.after(10000, stop)
    progressbar.start(100)


button = tk.Button(app, text='Start', width=25, command=start)
button.pack()

exit_button = tk.Button(app, text='Close', width=25, command=app.destroy)
exit_button.pack()

app.mainloop()
