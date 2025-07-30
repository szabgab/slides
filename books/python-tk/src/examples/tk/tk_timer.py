import tkinter as tk
import datetime

def timer():
    print(datetime.datetime.now())
    app.after(1000, timer)

app = tk.Tk()
app.title('Timer')

app.after(1000, timer)

exit_button = tk.Button(app, text="Exit", fg="red", command=app.destroy)
exit_button.pack()

app.mainloop()
