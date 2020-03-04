def check():
    for loc in hanoi.keys():
        if hanoi[loc] != sorted(hanoi[loc], reverse=True):
            raise Exception(f"Incorrect order in {loc}: {hanoi[loc]}")

def move(depth, source, target, helper):
    check()

    if not source or not depth:
        return True
    if len(hanoi[source]) < depth:
        raise Exception(f"source {source}: {hanoi[source]}  {depth}")

    if depth == 1:
        val = hanoi[source].pop()
        hanoi[target].append(val)
        print(f"x Move {val} from {source} to {target}")
    else:
        move(depth-1, source, helper, target)
        val = hanoi[source].pop()
        hanoi[target].append(val)
        print(f"y Move {val} from {source} to {target}")
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

