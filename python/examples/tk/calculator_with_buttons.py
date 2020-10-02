import tkinter as tk

app = tk.Tk()
app.title('Calculator')

label = tk.Label(app,
    width=50,
    #height=2,
    font=['Curier', 20],
    bg='white',
)
label.pack()

def backspace():
    if len(label['text']) > 0:
        label['text'] = label['text'][0:-1]

def clear():
    label['text'] = ''

def calc():
    inp = label['text']
    print(inp)
    out = eval(inp)
    label['text'] = out

def close():
    app.destroy()
    exit()

def enter(value):
    label['text'] += value

def add_button(num, frame):
    btn = tk.Button(frame, text=num, width=25, command=lambda : enter(num))
    btn.pack(side="left")
    buttons[num] = btn

numbers_frame = tk.Frame(app)
numbers_frame.pack()
numbers_row = {}
numbers_row[1] = tk.Frame(numbers_frame)
numbers_row[1].pack(side="top")
numbers_row[2] = tk.Frame(numbers_frame)
numbers_row[2].pack(side="top")
numbers_row[3] = tk.Frame(numbers_frame)
numbers_row[3].pack(side="top")
ops_row = tk.Frame(numbers_frame)
ops_row.pack(side="top")

buttons = {}

add_button('1', numbers_row[1])
add_button('2', numbers_row[1])
add_button('3', numbers_row[1])
add_button('4', numbers_row[2])
add_button('5', numbers_row[2])
add_button('6', numbers_row[2])
add_button('7', numbers_row[3])
add_button('8', numbers_row[3])
add_button('9', numbers_row[3])


for op in ['+', '-', '*', '/']:
    add_button(op, ops_row)


calc_btn = tk.Button(app, text='=', command=calc)
calc_btn.pack()

clear_btn = tk.Button(app, text='C', command=clear)
clear_btn.pack()

backspace_btn = tk.Button(app, text='Bksp', command=backspace)
backspace_btn.pack()


close_btn = tk.Button(app, text='Close', width=25, fg='red', command=close)
close_btn.pack()

app.mainloop()

