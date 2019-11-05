#!/usr/bin/env python

from tkinter import Tk, Frame, Button, Label, Entry

class Example(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.createWidgets()

    def say_hi(self):
        print("hi there, everyone! ")
        print("Name: {}".format(self.name.get()))
        print("Password: {}".format(self.password.get()))
        self.password.delete(0, 'end')


    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        # Simple Label widget:
        self.name_title = Label(self, text="Name:")
        self.name_title.pack({"side": "left"})

        # Simple Entry widget:
        self.name = Entry(self)
        self.name.pack({"side": "left"})
        self.name.insert(0, "Your name")

        # Simple Label widget:
        self.password_title = Label(self, text="Password:")
        self.password_title.pack({"side": "left"})

        # In order to hide the text as it is typed (e.g. for Passwords)
        # set the "show" parameter:
        self.password = Entry(self)
        self.password["show"] = "*"
        self.password.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

def main():
    root = Tk()
    app = Example(parent=root)

    root.lift()
    root.call('wm', 'attributes', '.', '-topmost', True)
    root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)

    app.mainloop()

main()  


