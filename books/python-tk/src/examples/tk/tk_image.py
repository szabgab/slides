import tkinter as tk
import os
import sys
from PIL import Image, ImageTk

if len(sys.argv) != 2:
   exit(f"Usage: {sys.argv[0]} PATH_TO_IMAGE")
file_path = sys.argv[1]

app = tk.Tk()
app.title('Show image')


#img = tk.PhotoImage(file=file_path) # only seems to handle png and gif

# Tried with png, jpg, gif
img = ImageTk.PhotoImage(Image.open(file_path))
img_width = img.width()
img_height = img.height()

canvas = tk.Canvas(app, width = img_width, height = img_height)
canvas.pack()
img_on_canvas = canvas.create_image(img_width/2, img_height/2, image=img)

app.mainloop()

