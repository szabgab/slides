from tkinter import filedialog

input_file = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("Any file", "*")))
output_file = filedialog.asksaveasfilename(filetypes=(("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("Any file", "*")))

print(f"This code will read {input_file}, analyze it and then create {output_file}")

