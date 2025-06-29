def check():
    for loc in hanoi.keys():
        if hanoi[loc] != sorted(hanoi[loc], reverse=True):
            raise Exception(f"Incorrect order in {loc}: {hanoi[loc]}")

def move(depth, source, target, helper):
    if depth > 0:
        move(depth-1, source, helper, target)

        val = hanoi[source].pop()
        hanoi[target].append(val)
        print(f"Move {val} from {source} to {target}   Status A:{str(hanoi['A']):10}  B:{str(hanoi['B']):10}  C:{str(hanoi['C']):10}")
        check()

        move(depth-1, helper, target, source)
    check()

hanoi = {
    'A': [4, 3, 2, 1],
    'B': [],
    'C': [],
}

check()
move(len(hanoi['A']), 'A', 'C', 'B')
check()

