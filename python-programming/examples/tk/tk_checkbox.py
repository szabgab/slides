import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack()
        self.createWidgets()

    def show_values(self):
        print("show values")
        for v in self.vars:
            print(v.get())

    def createWidgets(self):
        self.QUIT = tk.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})


        self.vars = []
        self.cbs = []
        self.vars.append(tk.IntVar())
        cb = tk.Checkbutton(text="Blue", variable=self.vars[-1])
        cb.pack({"side": "left"})
        self.cbs.append(cb)

        self.vars.append(tk.IntVar())
        cb = tk.Checkbutton(text="Yellow", variable=self.vars[-1])
        cb.pack({"side": "left"})
        self.cbs.append(cb)

        self.show = tk.Button(self)
        self.show["text"] = "Show",
        self.show["command"] = self.show_values
        self.show.pack({"side": "left"})

def main():
    root = tk.Tk()
    app = Example(parent=root)

    root.lift()
    root.call('wm', 'attributes', '.', '-topmost', True)
    root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)

    app.mainloop()

main()
