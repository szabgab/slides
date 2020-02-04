import tkinter as tk


def say_hi():
    print("hi there, everyone! ")
    print("Name: {}".format(name.get()))
    print("Password: {}".format(password.get()))
    print("count: {}".format(count.get()))
    password.delete(0, 'end')

def close_app():
    app.destroy()
    exit()

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

# QUIT = tk.Button(app)
# QUIT["text"] = "QUIT"
# QUIT["fg"]   = "red"
# QUIT["command"] =  close_app
# QUIT.pack({"side": "left"})

app.mainloop()


# self.count = tk.IntVar()
# self.count.set(2)
# self.my_radio = []
# radio = [(1, "One"), (2, "Two"), (3, "Three")]
# for ix in range(len(radio)):
#     self.my_radio.append(tk.Radiobutton(self, text=radio[ix][1], variable=self.count, value=radio[ix][0]))
#     self.my_radio[ix].pack({"side": "bottom"})
# 
# 
# self.hi_there = tk.Button(self)
# self.hi_there["text"] = "Hello",
# self.hi_there["command"] = self.say_hi
# 
# self.hi_there.pack({"side": "left"})

