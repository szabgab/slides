import tkinter as tk
from tkinter import simpledialog

class MyDialog(tk.simpledialog.Dialog):
    def __init__(self, parent, title):
        self.my_username = None
        self.my_password = None
        super().__init__(parent, title)

    def body(self, frame):
        # print(type(frame)) # tkinter.Frame
        self.my_username_label = tk.Label(frame, width=25, text="Username")
        self.my_username_label.pack()
        self.my_username_box = tk.Entry(frame, width=25)
        self.my_username_box.pack()

        self.my_password_label = tk.Label(frame, width=25, text="Passworde")
        self.my_password_label.pack()
        self.my_password_box = tk.Entry(frame, width=25)
        self.my_password_box.pack()
        self.my_password_box['show'] = '*'

        return frame

    def ok_pressed(self):
        # print("ok")
        self.my_username = self.my_username_box.get()
        self.my_password = self.my_password_box.get()
        self.destroy()

    def cancel_pressed(self):
        # print("cancel")
        self.destroy()


    def buttonbox(self):
        self.ok_button = tk.Button(self, text='OK', width=5, command=self.ok_pressed)
        self.ok_button.pack(side="left")
        cancel_button = tk.Button(self, text='Cancel', width=5, command=self.cancel_pressed)
        cancel_button.pack(side="right")
        self.bind("<Return>", lambda event: self.ok_pressed())
        self.bind("<Escape>", lambda event: self.cancel_pressed())

def mydialog(app):
    dialog = MyDialog(title="Login", parent=app)
    return dialog.my_username, dialog.my_password


def main():
    app.title('Dialog')

    string_button = tk.Button(app, text='Show', width=25, command=show_dialog)
    string_button.pack()

    exit_button = tk.Button(app, text='Close', width=25, command=app.destroy)
    exit_button.pack()

    app.mainloop()

def show_dialog():
    answer = mydialog(app)
    # print(type(answer)) # tuple
    print(answer)

app = tk.Tk()

main()    


