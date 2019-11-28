import re

text = "This is 1 string with 3 numbers: 34"
new_text = re.sub(r'(\d+)', r'\1\1', text)
print(new_text)   # This is 11 string with 33 numbers: 3434

double_numbers = re.sub(r'(\d+)', lambda match: str(2 * int(match.group(0))), text)
print(double_numbers)  # This is 2 string with 6 numbers: 68

