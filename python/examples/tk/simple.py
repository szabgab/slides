from Tkinter import Tk, Frame, BOTH


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(parent=root)

    # move the window to the front (needed on Mac only?)
    root.lift()
    root.call('wm', 'attributes', '.', '-topmost', True)
    root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)

    root.mainloop()  

main()  

