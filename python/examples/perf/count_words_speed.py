from collections import defaultdict
from collections import Counter
import timeit

def generate_list_of_words(number, repeat):
    #words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']
    words = []
    for ix in range(number):
        for _ in range(repeat):
            words.append(str(ix))
    return words

def plain_counter(words):
    counter = {}
    for word in words:
        if word not in counter:
            counter[word] = 0
        counter[word] += 1
    return counter

def counter_with_exceptions(words):
    counter = {}
    for word in words:
        try:
            counter[word] += 1
        except KeyError:
           counter[word] = 1
    return counter


def counter_with_counter(words):
    counter = Counter()
    for word in words:
       counter[word] += 1
    return counter

def counter_with_default_dict(words):
    counter = defaultdict(int)
    for word in words:
       counter[word] += 1
    return counter


def main():
    #words = generate_list_of_words(1000, 1)

    #counter = plain_counter(words)
    #counter = counter_with_counter(words)
    #counter = counter_with_default_dict(words)
    #counter = counter_with_exceptions(words)
    #for word in sorted(counter.keys()):
    #   print("{}:{}".format(word, counter[word]))

    for repeat in [1, 10, 20, 50]:
        different = int(1000 / repeat)
        print(f'repeat {repeat}  different {different}')
        for name in ['plain_counter', 'counter_with_counter', 'counter_with_default_dict', 'counter_with_exceptions']:
            print("{:26} {}".format(name, timeit.timeit(f'{name}(words)',
                number=10000,
                setup=f'from __main__ import {name}, generate_list_of_words; words = generate_list_of_words({different}, {repeat})')))
        print()

if __name__ == "__main__":
    main()

