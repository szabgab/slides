import tkinter as tk
from tkinter import filedialog

input_file_path = None
output_file_path = None

def run_process():
    print("Parameters:")
    print(f"in: {input_file_path}")
    print(f"out: {output_file_path}")

def close_app():
    print("Bye")
    app.destroy()

def select_input_file():
    global input_file_path
    input_file_path = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("Any file", "*")))
    print(input_file_path)

def select_output_file():
    global output_file_path
    output_file_path = filedialog.asksaveasfilename(filetypes=(("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("Any file", "*")))
    print(output_file_path)

app = tk.Tk()
app.title('Convert file')

input_button = tk.Button(app, text='Select input file', command=select_input_file)
input_button.pack()

output_button = tk.Button(app, text='Select output file', command=select_output_file)
output_button.pack()

process_button = tk.Button(app, text='Process', width=25, command=run_process)
process_button.pack()

exit_button = tk.Button(app, text='Close', width=25, command=close_app)
exit_button.pack()

app.mainloop()


