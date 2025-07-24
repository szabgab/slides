from typing import Union, Optional

text = "a,b,c"

print(text.split())
print(text.split(None))
print(text.split(","))


#def split(text, sep: str | None=None):
#def split(text, sep: Union[str,None]=None):
def split(text, sep: Optional[str]=None):
    return text.split(sep)

print(split(text))
print(split(text, None))
print(split(text, ","))
print(split(text, 42))
