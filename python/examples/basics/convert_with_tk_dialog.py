from tkinter import filedialog

# On recent versions of Ubuntu you might need to install python3-tk in addition to python3 using
# sudo apt-get install python3-tk

input_file = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("Any file", "*")))
output_file = filedialog.asksaveasfilename(filetypes=(("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("Any file", "*")))

print(f"This code will read {input_file}, analyze it and then create {output_file}")

