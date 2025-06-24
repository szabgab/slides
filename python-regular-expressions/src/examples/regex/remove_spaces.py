line = "  ab cd  "

res = line.lstrip(" ")
print(f"'{res}'")        # 'ab cd  '

res = line.rstrip(" ")
print(f"'{res}'")        # '  ab cd'

res = line.strip(" ")
print(f"'{res}'")        # 'ab cd'

res = line.replace(" ", "")
print(f"'{res}'")        # 'abcd'

