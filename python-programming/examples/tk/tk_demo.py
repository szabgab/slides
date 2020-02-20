import tkinter as tk
from tkinter import messagebox, filedialog
import os


def scary_action():
    messagebox.showerror(title="Scary", message="Deleting hard disk. Please wait...")


def run_code():
    text = ""
    text += "Name: {}\n".format(name.get())
    text += "Password: {}\n".format(password.get())
    text += "Animal: {}\n".format(animal.get())
    text += "Colors: "
    for ix in range(len(colors)):
        if colors[ix].get():
            text += color_names[ix] + " "
    text += "\n"
    text += "Filename: {}\n".format(os.path.basename(filename_entry.get()))

    resp = messagebox.askquestion(title="Running with", message=f"Shall I start running with the following values?\n\n{text}")
    if resp == 'yes':
        output_window['state'] = 'normal'  # allow editing of the Text widget
        output_window.insert('end', f"{text}\n--------\n")
        output_window['state'] = 'disabled'  # disable editing
        output_window.see('end')  # scroll to the end as we make progress
        app.update()


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
# name.insert(0, "Your name")

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


def open_filename_selector():
    file_path = filedialog.askopenfilename(filetypes=(("Any file", "*"),))
    filename_entry.delete(0, tk.END)
    filename_entry.insert(0, file_path)


filename_frame = tk.Frame(app)
filename_frame.pack()
filename_label = tk.Label(filename_frame, text="Filename:", width=10)
filename_label.pack({"side": "left"})
filename_entry = tk.Entry(filename_frame, width=60)
filename_entry.pack({"side": "left"})
filename_button = tk.Button(filename_frame, text="Select file", command=open_filename_selector)
filename_button.pack({"side": "left"})

output_frame = tk.Frame(app)
output_frame.pack()
output_window = tk.Text(output_frame, state='disabled')
output_window.pack()


buttons = tk.Frame(app)
buttons.pack()

scary_button = tk.Button(buttons, text="Don't click here!", fg="red", command=scary_action)
scary_button.pack({"side": "left"})

action_button = tk.Button(buttons, text="Run", command=run_code)
action_button.pack()

app.mainloop()
