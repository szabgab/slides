import tkinter as tk

app = tk.Tk()
app.title('Menu')

def run_new():
    print("new")

def run_exit():
    print("exit")
    app.destroy()
    exit()

def enable_languages():
    menu2.entryconfig("Klingon", state="normal")
def disable_languages():
    menu2.entryconfig("Klingon", state="disabled")

def set_language(lang):
    print(lang)


menubar = tk.Menu(app)

menu1 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", underline=0, menu=menu1)
menu1.add_command(label="New", command=run_new)
menu1.add_command(label="Enable language", command=enable_languages)
menu1.add_command(label="Disable language", command=disable_languages)
menu1.add_separator()
menu1.add_command(label="Exit", underline=1, command=run_exit)

menu2 = tk.Menu(menubar, tearoff=1)
menubar.add_cascade(label="Language", menu=menu2)
menu2.add_command(label="English")
menu2.add_command(label="Hebrew")
menu2.add_command(label="Spanish")
menu2.add_command(label="Klingon", state="disabled", command=lambda : set_language('Klingon'))
menu2.add_command(label="Hungarian")

app.config(menu=menubar)

app.mainloop()

