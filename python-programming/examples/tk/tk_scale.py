import tkinter as tk

def run_action():
    h = scale_h.get()
    print(h)

    v = scale_v.get()
    print(v)

app = tk.Tk()
app.title('Scale')

scale_h = tk.Scale(app, from_=0, to=42, orient=tk.HORIZONTAL)
scale_h.pack()

scale_v = tk.Scale(app, from_=1, to=100, orient=tk.VERTICAL)
scale_v.pack()
scale_v.set(23)

action_button = tk.Button(app, text='Action', width=25, command=run_action)
action_button.pack()

app.mainloop()

