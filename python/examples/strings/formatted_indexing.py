txt = "Some text"
num = 42.12

print("'{}'{}'".format(txt, num))   # 'Some text'42.12'
print("'{0}'{1}'".format(txt, num)) # 'Some text'42.12'

print("'{1}'{0}'".format(txt, num)) # '42.12'Some text'
print("'{0}'{0}'".format(txt, num)) # 'Some text'Some text'
