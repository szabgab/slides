import tkinter as tk

app = tk.Tk()
app.title('Single Button')

button = tk.Button(app,
    text='Close',
    width=25,
    command=app.destroy,
    #bg='lightblue',
)
button.pack()

app.mainloop()
