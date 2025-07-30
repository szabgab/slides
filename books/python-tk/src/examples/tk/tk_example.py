import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack()
        self.createWidgets()

    def say_hi(self):
        print("hi there, everyone! ")
        print("Name: {}".format(self.name.get()))
        print("Password: {}".format(self.password.get()))
        print("count: {}".format(self.count.get()))
        self.password.delete(0, 'end')


    def createWidgets(self):
        self.QUIT = tk.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        # Simple Label widget:
        self.name_title = tk.Label(self, text="Name:")
        self.name_title.pack({"side": "left"})

        # Simple Entry widget:
        self.name = tk.Entry(self)
        self.name.pack({"side": "left"})
        self.name.insert(0, "Your name")

        # Simple Label widget:
        self.password_title = tk.Label(self, text="Password:")
        self.password_title.pack({"side": "left"})

        self.count = tk.IntVar()
        self.count.set(2)
        self.my_radio = []
        radio = [(1, "One"), (2, "Two"), (3, "Three")]
        for ix in range(len(radio)):
            self.my_radio.append(tk.Radiobutton(self, text=radio[ix][1], variable=self.count, value=radio[ix][0]))
            self.my_radio[ix].pack({"side": "bottom"})

        # In order to hide the text as it is typed (e.g. for Passwords)
        # set the "show" parameter:
        self.password = tk.Entry(self)
        self.password["show"] = "*"
        self.password.pack({"side": "left"})

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

def main():
    root = tk.Tk()
    app = Example(parent=root)

    root.lift()
    root.call('wm', 'attributes', '.', '-topmost', True)
    root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)

    app.mainloop()

main()
