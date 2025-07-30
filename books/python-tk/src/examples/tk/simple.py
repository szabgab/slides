import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=tk.BOTH, expand=1)

def main():
    app = tk.Tk()
    app.geometry("250x150+300+300")
    main_frame = Example(parent=app)

    # move the window to the front (needed on Mac only?)
    app.lift()
    app.call('wm', 'attributes', '.', '-topmost', True)
    app.after_idle(app.call, 'wm', 'attributes', '.', '-topmost', False)

    app.mainloop()

main()

