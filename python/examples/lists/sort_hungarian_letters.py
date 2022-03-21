letters = [
    "a", "á", "b", "c", "cs", "d", "dz", "dzs", "e", "é", "f",
    "g", "gy", "h", "i", "í", "j", "k", "l", "ly", "m", "n",
    "ny", "o", "ó", "ö", "ő", "p", "q", "r", "s", "sz", "t",
    "ty", "u", "ú", "ü", "ű", "v", "w", "x", "y", "z", "zs",
]
#print(dict(enumerate(letters)))
mapping = {v:k for k, v in dict(enumerate(letters)).items()}
print(mapping)
print('------------------')

text = ["cs", "á", "ő", "ú", "e", "dzs", "zs", "a", "ny"]
print(sorted(text))
print(sorted(text, key=lambda letter: mapping[letter]))

