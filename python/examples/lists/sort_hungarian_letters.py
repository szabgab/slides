letters = [
    "a", "á", "b", "c", "cs", "d", "dz", "dzs", "e", "é", "f",
    "g", "gy", "h", "i", "í", "j", "k", "l", "ly", "m", "n",
    "ny", "o", "ó", "ö", "ő", "p", "q", "r", "s", "sz", "t",
    "ty", "u", "ú", "ü", "ű", "v", "w", "x", "y", "z", "zs",
]
print(enumerate(letters))
print('-------')
print(list(enumerate(letters)))
print('-------')
print(dict(enumerate(letters)))
print('-------')
#mapping = {v:k for k, v in dict(enumerate(letters)).items()}
mapping = {letter:ix for ix, letter in enumerate(letters)}
print(mapping)
print('------------------')

text = ["cs", "á", "ő", "ú", "e", "dzs", "zs", "a", "ny"]
print(sorted(text))
print('------------------')
print(sorted(text, key=lambda letter: mapping[letter]))

