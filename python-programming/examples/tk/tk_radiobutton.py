import tkinter as tk

def run_action():
    print("clicked")
    print(count.get())

app = tk.Tk()
app.title('Radio button')

count = tk.IntVar()
#count.set(2)

my_radios = []
values = [(1, "One"), (2, "Two"), (3, "Three")]
for ix in range(len(values)):
    my_radios.append(tk.Radiobutton(app, text=values[ix][1], variable=count, value=values[ix][0]))
    my_radios[ix].pack()

action_button = tk.Button(app, text='Action', width=25, command=run_action)
action_button.pack()

exit_button = tk.Button(app, text='Close', width=25, command=app.destroy)
exit_button.pack()

app.mainloop()
