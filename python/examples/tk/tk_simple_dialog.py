import tkinter as tk
from tkinter import simpledialog

def main():
    app.title('Dialog')

    string_button = tk.Button(app, text='Ask for string', width=25, command=ask_for_string)
    string_button.pack()

    int_button = tk.Button(app, text='Ask for int', width=25, command=ask_for_int)
    int_button.pack()

    float_button = tk.Button(app, text='Ask for float', width=25, command=ask_for_float)
    float_button.pack()

    exit_button = tk.Button(app, text='Close', width=25, command=app.destroy)
    exit_button.pack()

    app.mainloop()

def ask_for_string():
    answer = simpledialog.askstring("Input", "Type a string:", parent=app)
    print(type(answer))
    print(answer)

def ask_for_int():
    answer = simpledialog.askinteger("Input", "Type an int:", parent=app)
    print(type(answer))
    print(answer)

def ask_for_float():
    answer = simpledialog.askfloat("Input", "Type a float", parent=app)
    print(type(answer))
    print(answer)


app = tk.Tk()

main()    


