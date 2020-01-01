import random


def f():
    n = 0
    for i in range(30):
        n += random.random()
    return n

def g():
    return random.random() * 30


def main(n):
    text = get_str(n)

    #print(str)
    text_sorted = sort(text)
    return text_sorted

def sort(s):
    chars = list(s)
    for i in reversed(range(len(chars))):
        a = f()
        b = g()
        for j in range(i, len(chars)-1):
            swap(chars, j)

    return ''.join(chars)

def get_str(n):
    text = ''
    for i in xrange(1, n):
        text += chr(65 + random.randrange(0, 26))
    return text

def swap(lst, loc):
    if lst[loc] > lst[loc + 1]:
        lst[loc], lst[loc + 1] = lst[loc + 1], lst[loc]

if __name__ == '__main__':
    print(main(1000))

