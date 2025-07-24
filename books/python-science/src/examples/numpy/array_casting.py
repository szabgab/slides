import numpy as np

a = np.array([
    [ "12",  "23",  "3",  "4"],
    [ "2",  "3",  "4",  "5"]
])

print(a)
#[['12' '23' '3' '4']
# ['2' '3' '4' '5']]

try:
    b = a + 1
except Exception as e:
    print(e)
# TypeError: ufunc 'add' did not contain a loop with
#    signature matching types dtype('<U3') dtype('<U3') dtype('<U3')


c = a.astype(np.int) + 1
print(c)
# [[13 24  4  5]
# [ 3  4  5  6]]
