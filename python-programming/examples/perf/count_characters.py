# changes chars and counter
def add_char(chars, counter, ch, cnt=1):
    for ix in range(len(chars)):
        if chars[ix] == ch:
            counter[ix] += cnt
            break
    else:
        chars.append(ch)
        counter.append(cnt)


def count_in_file(filename):
    #print(filename)
    chars   = []
    counter = []
    with open(filename) as fh:
        for row in fh:
            for ch in row:
                #print(ch)
                if ch == ' ':
                    continue
                if ch == '\n':
                    continue
                add_char(chars, counter, ch)

    #print(chars)
    #print(counter)
    return chars, counter

def merge(chars1, counter1, chars2, counter2):
    chars = []
    counter = []
    for ix in range(len(chars1)):
        add_char(chars, counter, chars1[ix], cnt=counter1[ix])
    for ix in range(len(chars2)):
        add_char(chars, counter, chars2[ix], cnt=counter2[ix])
    return chars, counter


def print_results(chars, counter):
    print("Results")
    for ix in range(len(chars)):
        print("{}  {}".format(chars[ix], counter[ix]))

def count_in(filenames):
    total_chars = []
    total_counter = []
    for filename in filenames:
        chars, counter = count_in_file(filename)
        total_chars, total_counter = merge(total_chars, total_counter, chars, counter)

    return total_chars, total_counter


if __name__ == '__main__':
    import sys
    chars, counter = count_in(sys.argv[1:])
    print_results(chars, counter)
