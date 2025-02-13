
def print_series(series):
    #started = False;
    for val in series:
        if val > 10:
        #    started = True
            print("start new series")
            print(val)

        #if not started:
        #    continue

        if val <= 10:
            print(val)


print_series([20, 2, 3, 30, 1, 7])
print()
print_series([1, 4, 20, 2, 3, 30, 1, 7])
