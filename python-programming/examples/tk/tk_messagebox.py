import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title('Menu')

def run_show_info():
    messagebox.showinfo(title = "Title", message = "Show info text")

def run_show_warning():
    messagebox.showwarning(title = "Title", message = "Show warning text")

def run_show_error():
    messagebox.showerror(title = "Title", message = "Show error text")

def run_ask_question():
    resp = messagebox.askquestion(title = "Title", message = "Can I ask you a question?")
    print(resp)  # "yes" / "no" (default "no")

def run_ask_okcancel():
    resp = messagebox.askokcancel(title = "Title", message = "Shall I do it?")
    print(resp)  # True / False (default = False)

def run_ask_retrycancel():
    resp = messagebox.askretrycancel(title = "Title", message = "Shall retry it?")
    print(resp)  # True / False (default = False)

def run_ask_yesno():
    resp = messagebox.askyesno(title = "Title", message = "Yes or No?")
    print(resp)  # True / False (default = False)

def run_ask_yesnocancel():
    resp = messagebox.askyesnocancel(title = "Title", message = "Yes, No, or Cancel?")
    print(resp)  # True / False / None (default = None)

def run_exit():
    app.destroy()


menubar = tk.Menu(app)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Info",    underline=0, command=run_show_info)
menu1.add_command(label="Warning", underline=0, command=run_show_warning)
menu1.add_command(label="Error",   underline=0, command=run_show_error)
menu1.add_separator()
menu1.add_command(label="Exit", underline=1, command=run_exit)

menubar.add_cascade(label="Show", underline=0, menu=menu1)

menu2 = tk.Menu(menubar, tearoff=0)
menu2.add_command(label="Question",           underline=0, command=run_ask_question)
menu2.add_command(label="OK Cancel",          underline=0, command=run_ask_okcancel)
menu2.add_command(label="Retry Cancel",       underline=0, command=run_ask_retrycancel)
menu2.add_command(label="Yes or No",          underline=0, command=run_ask_yesno)
menu2.add_command(label="Yes, No, or Cancel", underline=5, command=run_ask_yesnocancel)

menubar.add_cascade(label="Ask", underline=0, menu=menu2)

app.config(menu=menubar)

app.mainloop()

