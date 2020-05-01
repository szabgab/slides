
filename = __file__ # just being lazy and using ourselves as the input file

with open(filename) as fh:
    length = map(len, fh)
    print(length)
    for ln in length:
        print(ln)
        # if ln > 10:
        #     break
