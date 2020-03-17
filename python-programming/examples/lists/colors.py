colors = ['blue', 'yellow', 'black', 'purple']
for i in range(len(colors)):
    print("{}) {}".format(i+1, colors[i]))

c = int(input("Select color ")) - 1
print(colors[c])
