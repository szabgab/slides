from counter import Counter

cnt = Counter()

for i in cnt:
    print(f"i: {i}")
    try:
        n = next(cnt)
        print(f"n: {n}")
    except Exception as ex:
        print(ex.__class__.__name__)
        break
