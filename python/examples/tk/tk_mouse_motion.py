import tkinter as tk

app = tk.Tk()
app.title('Key binding')

label = tk.Label(app, text='Click the buttons of the mouse on the window')
label.config(font=("Courier", 44))
label.pack()

def action(event):
    #print(dir(event))
    print(f"{event.x} - {event.y}")

app.bind("<B1-Motion>", action)
app.bind("<B2-Motion>", action)
app.bind("<B3-Motion>", action)


app.mainloop()
