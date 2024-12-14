text = "a,b,c"

print(text.split())
print(text.split(None))
print(text.split(","))




def split(text, sep: str | None=None):
    return text.split(sep)

print(split(text))
print(split(text, None))
print(split(text, ","))
