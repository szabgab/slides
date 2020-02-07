import tkinter as tk

def run_action():
    color = color_var.get()
    print(color)

    size = size_var.get()
    print(size)

app = tk.Tk()
app.title('Option Menu')

color_var = tk.StringVar(app)
color_selector = tk.OptionMenu(app, color_var, "Red", "Green", "Blue")
color_selector.pack()

sizes = ("Small", "Medium", "Large")
size_var = tk.StringVar(app)
size_selector = tk.OptionMenu(app, size_var, *sizes)
size_selector.pack()

action_button = tk.Button(app, text='Action', width=25, command=run_action)
action_button.pack()

app.mainloop()
