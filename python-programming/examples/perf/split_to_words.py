import sys
import re

def split_to_words_by_regex(text):
    return re.split(' ', text)

def split_to_words_by_split(text):
    return text.split(' ')

def split_to_words_by_chars(text):
    words = []
    word = ''
    for ch in text:
        if ch == ' ':
            words.append(word)
            word = ''
        else:
            word += ch
    if word:
        words.append(word)
    return words


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")

    filename = sys.argv[1]
    with open(filename) as fh:
        text = fh.read()
    res1 = split_to_words_by_split(text)
    res2 = split_to_words_by_chars(text)
    res3 = split_to_words_by_regex(text)
    #print(res1)
    #print(res2)
    assert res1 == res2
    assert res1 == res3
