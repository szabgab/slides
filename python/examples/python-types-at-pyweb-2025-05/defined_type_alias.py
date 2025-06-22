LabelType = str
OtherType = str

def f(x: OtherType):
    print(x)

txt = "hello"
label: LabelType = txt

print(label)
f(txt)
f(label)


