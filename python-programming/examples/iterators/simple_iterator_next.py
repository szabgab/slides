from counter import Counter

cnt = Counter()

while True:
    try:
        a = next(cnt)
        print(a)
    except Exception as ex:
        print(ex.__class__.__name__)
        break