import tkinter as tk
import random
from tkinter.colorchooser import askcolor


def callback():
    red = random.randrange(0, 255)
    green = random.randrange(0, 255)
    blue = random.randrange(0, 255)
    print(f"red: {red}")
    print(f"green: {green}")
    print(f"blue: {blue}")
    color = f"#{red:02X}{green:02X}{blue:02X}"
    print(color)
    floating, hexa = askcolor(color=color,
                      title="Color Chooser")
    print(floating)
    print(hexa)
    if hexa is not None:
        print('red ', int(hexa[1:3], 16))
        print('green ', int(hexa[1:3], 16))
        print('blue ', int(hexa[1:3], 16))

root = tk.Tk()
tk.Button(root,
          text='Choose Color',
          fg="darkgreen",
          command=callback).pack(side=tk.LEFT, padx=10)
tk.Button(text='Quit',
          command=root.quit,
          fg="red").pack(side=tk.LEFT, padx=10)
tk.mainloop()

# Based on https://www.python-course.eu/tkinter_dialogs.php