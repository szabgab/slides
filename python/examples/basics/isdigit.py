
for var in ["23", "2.3", "a", "2.3.4"]:
    print(var)
    if var.isdigit():
        print(f"{var} can be converted to int:", int(var))
    if var.replace(".", "", 1).isdigit():
        print(f"{var} can be converted to float:", float(var))
    print('-----')




