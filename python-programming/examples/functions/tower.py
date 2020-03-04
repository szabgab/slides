
#def move(source, depth, target, helper):
#    #if helper:
#    #   raise Exception("Helper is in use already")
#    if not source or not depth:
#        return True
#    if len(source) < depth:
#        raise Exception("There are not enough")
#    if depth == 1:
#        if len(source) == 1:
#            if target and target[-1] > source[-1]:
#                raise Exception('Cannot move')
#            target.append(source.pop())
#        else:
#            if helper and helper[-1] > source[-1]:
#                raise Exception('Cannot move')
#            helper.append(source.pop())
#            move(source, depth-1, helper=target, target=helper)
#        return True
#
#    
#
#    if len(source) == 1:
#        if target and target[-1] > source[-1]:
#            raise Exception('Cannot move')
#        target.append(source.pop())
#    else:
#        if helper and helper[-1] > source[-1]:
#            raise Exception('Cannot move')
#        helper.append(source.pop())
#        move(



def check():
    for loc in hanoi.keys():
        if hanoi[loc] != sorted(hanoi[loc], reverse=True):
            raise Exception(f"Incorrect order in {loc}: {hanoi[loc]}")

def move(source, target, helper):
    check()

    if not source:
        return True
    if len(hanoi[source]) == 1:
        val = hanoi[source].pop()
        hanoi[target].append(val)
        print(f"a Move {val} from {source} to {target}")
    elif len(hanoi[source]) == 2:
        val = hanoi[source].pop()
        hanoi[helper].append(val)
        print(f"b Move {val} from {source} to {helper}")
        check()
        val = hanoi[source].pop()
        hanoi[target].append(val)
        print(f"b Move {val} from {source} to {target}")
        check()
        val = hanoi[helper].pop()
        hanoi[target].append(val)
        print(f"b Move {val} from {helper} to {target}")
        check()
    else:
        val = hanoi[source].pop()
        hanoi[helper].append(val)
        print(f"c Move {val} from {source} to {helper}")
        move(source, helper, target)

hanoi = {
    'A': [3, 2, 1],
    'B': [],
    'C': [],
}

check()
move('A', 'C', 'B')
check()

