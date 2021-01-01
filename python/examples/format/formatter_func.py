

def formatter(value, filler, width):
    return "{var:{fill}>{width}}".format(var=value, fill=filler, width=width)

text = formatter(23, "0", 7)
print(text)


print(formatter(42, " ", 7))
print(formatter(1234567, " ", 7))
