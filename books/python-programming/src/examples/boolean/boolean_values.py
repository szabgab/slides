values = [None, 0, "", False, [], (), {}, "0", True]

for v in values:
    if v:
        print("True value:  ", v)
    else:
        print("False value: ", v)

# False value:  None
# False value:  0
# False value:
# False value:  False
# False value:  []
# False value:  ()
# False value:  {}
# True value:   0
# True value:   True

