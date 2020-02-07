import tkinter as tk
from tkinter import messagebox

def scary_action():
    messagebox.showerror(title = "Scary", message = "Deleting hard disk. Please wait...")

def run_code():
    text = ""
    text += "Name: {}\n".format(name.get())
    text += "Password: {}\n".format(password.get())
    text += "Animal: {}".format(animal.get())
    text += "Colors: "
    for ix in range(len(colors)):
        if colors[ix].get():
            text += color_names[ix] + " "
    text += "\n"

    messagebox.showinfo(title = "Running with", message = text)

def close_app():
    app.destroy()

app = tk.Tk()
app.title('Simple App')

menubar = tk.Menu(app)
app.config(menu=menubar)

menu1 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", underline=0, menu=menu1)
menu1.add_separator()
menu1.add_command(label="Exit", underline=1, command=close_app)

top_frame = tk.Frame(app)
top_frame.pack(side="top")
pw_frame = tk.Frame(app)
pw_frame.pack(side="top")

# Simple Label widget:
name_title = tk.Label(top_frame, text=" Name:", width=10, anchor="w")
name_title.pack({"side": "left"})

# Simple Entry widget:
name = tk.Entry(top_frame)
name.pack({"side": "left"})
#name.insert(0, "Your name")

# Simple Label widget:
password_title = tk.Label(pw_frame, text=" Password:", width=10, anchor="w")
password_title.pack({"side": "left"})

# In order to hide the text as it is typed (e.g. for Passwords)
# set the "show" parameter:
password = tk.Entry(pw_frame)
password["show"] = "*"
password.pack({"side": "left"})

radios = tk.Frame(app)
radios.pack()
animal = tk.StringVar()
animal.set("Red")
my_radio = []
animals = ["Cow", "Mouse", "Dog", "Car", "Snake"]
for animal_name in animals:
    radio = tk.Radiobutton(radios, text=animal_name, variable=animal, value=animal_name)
    radio.pack({"side": "left"})
    my_radio.append(radio)


checkboxes = tk.Frame(app)
checkboxes.pack()
colors = []
my_checkbox = []
color_names = ["Red", "Blue", "Green"]
for color_name in color_names:
    color_var = tk.BooleanVar()
    colors.append(color_var)
    checkbox = tk.Checkbutton(checkboxes, text=color_name, variable=color_var)
    checkbox.pack({"side": "left"})
    my_checkbox.append(checkbox)


buttons = tk.Frame(app)
buttons.pack()

scary_button = tk.Button(buttons)
scary_button["text"] = "Don't click here!"
scary_button["fg"]   = "red"
scary_button["command"] = scary_action
scary_button.pack({"side": "left"})

action_button = tk.Button(buttons)
action_button["text"] = "Run",
action_button["command"] = run_code
action_button.pack()


app.mainloop()

