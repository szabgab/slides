from tkinter import filedialog

input_file_path = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("Any file", "*")))
print(input_file_path)

input("Press ENTER to end the script...")
