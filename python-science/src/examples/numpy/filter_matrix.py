import numpy as np

names = np.array(['Mary', 'Bar', 'Joe', 'Jane'])
print(names)
print()

def has_ar(text):
    return "ar" in text
    # if "ar" in text:
        # return True
    # else:
        # return False

names_with_ar_selector = np.vectorize(has_ar)
names_with_ar_bool = names_with_ar_selector(names)
print(names_with_ar_bool)
print()

scores = np.array([
    [23, 37, 18, 97, 13, 40],
    [10, 15, 20, 30, 39, 50],
    [99, 20, 83, 42, 19, 31],
    [19, 11, 55, 78, 39, 27]
])

print(scores[names_with_ar_bool])