import tkinter as tk

def echo():
    print('echo')
    label['text'] = entry.get()

app = tk.Tk()
app.title('Echo')

entry = tk.Entry(app)
entry.pack()

label = tk.Label(app, text="", width=10, anchor="w")
label.pack()


echo_button = tk.Button(app, text="Echo", command=echo)
echo_button.pack()

exit_button = tk.Button(app, text="Exit", fg="red", command=app.destroy)
exit_button.pack()

app.mainloop()

