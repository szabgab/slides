#!/usr/bin/env python

import tkinter as tk
from tkinter import filedialog

class Example(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack()
        self.createWidgets()

    def get_file(self):
        file_path = filedialog.askopenfilename()
        print(file_path)
        self.filename.delete(0, tk.END)
        self.filename.insert(0, file_path)

    def run_process(self):
        print("Running a process on file {}".format(self.filename.get()))

    def createWidgets(self):
        self.QUIT = tk.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "right"})

        # Simple Label widget:
        self.filename_title = tk.Label(self, text="Fileame:")
        self.filename_title.pack({"side": "left"})

        # Simple Entry widget:
        self.filename = tk.Entry(self, width=120)
        self.filename.pack({"side": "left"})
        self.filename.delete(0, tk.END)

        self.selector = tk.Button(self)
        self.selector["text"] = "Select",
        self.selector["command"] = self.get_file
        self.selector.pack({"side": "left"})

        self.process = tk.Button(self)
        self.process["text"] = "Process",
        self.process["command"] = self.run_process
        self.process.pack({"side": "left"})


def main():
    root = tk.Tk()
    app = Example(parent=root)

    root.lift()
    root.call('wm', 'attributes', '.', '-topmost', True)
    root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)

    app.mainloop()

main()


