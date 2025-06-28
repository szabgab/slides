colors = ['blue', 'yellow', 'black', 'purple']
for ix in range(len(colors)):
    print("{}) {}".format(ix+1, colors[ix]))

selection = input("Select color: ")
if not selection.isdecimal():
    exit(f"We need a number between 1 and {len(colors)}")

if int(selection) < 1 or int(selection) > len(colors):
    exit(f"The number must be between 1 and {len(colors)}")

col = int(selection) - 1
print(colors[col])
