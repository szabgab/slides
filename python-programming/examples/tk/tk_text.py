import tkinter as tk

app = tk.Tk()
app.title('Text Editor')

text = tk.Text(app)
text.pack({"side": "bottom"})

app.mainloop()
