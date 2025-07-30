import tkinter as tk

def close():
    app.destroy()

def clicked(val):
    entry.insert(tk.END, val)

app = tk.Tk()
app.title('Frame')

entry = tk.Entry(app)
entry.pack()

frames = {}
frames[1] = tk.Frame(app)
frames[1].pack(side="top")
frames[2] = tk.Frame(app)
frames[2].pack(side="top")
frames[3] = tk.Frame(app)
frames[3].pack(side="top")

btn = {}

btn["a"] = tk.Button(frames[1], text="a", width=25, command=lambda : clicked("a"))
btn["a"].pack(side="left")

btn["b"] = tk.Button(frames[1], text="b", width=25, command=lambda : clicked("b"))
btn["b"].pack(side="left")

btn["c"] = tk.Button(frames[2], text="c", width=25, command=lambda : clicked("c"))
btn["c"].pack(side="left")

btn["d"] = tk.Button(frames[2], text="d", width=25, command=lambda : clicked("d"))
btn["d"].pack(side="left")

close_btn = tk.Button(frames[3], text='Close', width=25, command=close)
close_btn.pack(side="right", expand=0)

app.mainloop()

