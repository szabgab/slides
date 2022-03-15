text = ["abc", "bbc", "Acdc"]

def by_lower_case_version(word):
    return word.lower()

print(sorted(text))
print(sorted(text, key=lambda word: word.lower()))
print(sorted(text, key=by_lower_case_version))
