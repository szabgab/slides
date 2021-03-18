import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk

file_path = None

app = tk.Tk()
app.title('Show image')

def run_open():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=(("Image", "*.png *.jpg *.jpeg *.gif"), ("PNG", "*.png"), ("JPG", "*.jpg"), ("Any file", "*"),))
    if file_path and os.path.isfile(file_path):
        global img
        img = ImageTk.PhotoImage(Image.open(file_path))
        width = img.width()
        height = img.height()
        #print(width)
        #print(height)
        canvas.config(width=width, height=height)
        canvas.create_image(width/2, height/2, image=img)

def run_exit():
    print("exit")
    app.destroy()

menubar = tk.Menu(app)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Open", underline=0, command=run_open)
menu1.add_separator()
menu1.add_command(label="Exit", underline=1, command=run_exit)
menubar.add_cascade(label="File", underline=0, menu=menu1)

app.config(menu=menubar)

canvas = tk.Canvas(app, width = 600, height = 600)
canvas.pack()

app.mainloop()

