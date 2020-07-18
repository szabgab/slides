import tkinter as tk

app = tk.Tk()
app.title('Key binding')

label = tk.Label(app, text='Use the keyboard: (a, Ctr-b, Alt-c, F1, Alt-F4)')
label.config(font=("Courier", 44))
label.pack()

def pressed_a(event):
    print("pressed a")

def pressed_control_b(event):
    print("pressed Ctr-b")

def pressed_alt_c(event):
    print("pressed Alt-c")

def pressed_f1(event):
    print("pressed F1")

app.bind("<a>", pressed_a)
app.bind("<Control-b>", pressed_control_b)
app.bind("<Alt-c>", pressed_alt_c)
app.bind("<F1>", pressed_f1)


app.mainloop()
