def check():
    for loc in ['A', 'B', 'C']:
        print(f"{loc} {hanoi[loc]}", end=' ')
        if hanoi[loc] != sorted(hanoi[loc], reverse=True):
            raise Exception(f"Incorrect order in {loc}: {hanoi[loc]}")
    print('')

def move(source, target, helper):
    #if not hanoi[source]:
    #    return
    if len(hanoi[source]) == 1:
        disk = hanoi[source].pop()
        print(f"Move {disk} from {source} to {target}")
        hanoi[target].append(disk)
        return
    big_disk = hanoi[source].pop(0)   # pretend the biggest disk is not there
    move(source, helper, target)
    print(f"Move {big_disk} from {source} to {target}")
    move(helper, target, source)
    hanoi[target].insert(0, big_disk) # stop pretending
    check()


hanoi = {
    'A': [4, 3, 2, 1],
    'B': [],
    'C': [],
}

check()
move('A', 'C', 'B')
check()

