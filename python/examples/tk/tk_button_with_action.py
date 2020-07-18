import tkinter as tk

def run_action():
    print("clicked")

app = tk.Tk()
app.title('Single Button')

action_button = tk.Button(app, text='Action', width=25, command=run_action)
action_button.pack()
#action_button.pack(side="left")

exit_button = tk.Button(app, text='Close', width=25, command=app.destroy)
exit_button.pack()

app.mainloop()
