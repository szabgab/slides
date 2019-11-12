#!/usr/bin/env python

from tkinter import Tk, Frame, Button, Label, Entry

class Example(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # Simple Label widget:
        self.name_title = Label(self, text="Hello World!")
        self.name_title.pack({"side": "left"})

def main():
    root = Tk()
    app = Example(parent=root)

    root.lift()
    root.call('wm', 'attributes', '.', '-topmost', True)
    root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)

    app.mainloop()

main()


