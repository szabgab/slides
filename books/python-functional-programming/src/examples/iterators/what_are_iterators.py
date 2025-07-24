from collections.abc import Iterator, Iterable

a_string = "Hello World"
a_list   = ["Tiger", "Mouse"]
a_tuple  = ("Blue", "Red")
a_range  = range(10)
a_fh     = open(__file__)
a_map    = map(lambda x: x*2, a_list)

for thing in [a_string, a_list, a_tuple, a_range, a_map, a_fh]:
    print(thing.__class__.__name__)
    print(issubclass(thing.__class__, Iterator))
    print(issubclass(thing.__class__, Iterable))
    zorg = iter(thing)
    print(zorg.__class__.__name__)
    print(issubclass(zorg.__class__, Iterator))

    print()

a_fh.close()