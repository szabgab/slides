import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # Simple Label widget:
        self.name_title = tk.Label(self, text="Hello World!")
        self.name_title.pack({"side": "left"})

def main():
    root = tk.Tk()
    app = Example(parent=root)
    app.mainloop()

main()
