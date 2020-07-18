queue = []

while True:
    inp = input(":")
    inp = inp.rstrip("\n")

    if inp == 'x':
        for name in queue:
           print(name)
        exit()

    if inp == 's':
        print(len(queue))
        continue

    if inp == 'n':
        if len(queue) > 0:
            print("next is {}".format(queue.pop(0)))
        else:
            print("the queue is empty")
        continue

    queue.append(inp)
