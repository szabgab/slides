import tkinter as tk

def reverse(txt):
    return txt[::-1]

app = tk.Tk()
app.title('כפתור')

label = tk.Label(app, text = reverse('שלום טיקי'))
label.pack()

button = tk.Button(app,
    text = reverse('סגור'),
    width=25,
    command=app.destroy,
    #bg='lightblue',
)
button.pack()

app.mainloop()
