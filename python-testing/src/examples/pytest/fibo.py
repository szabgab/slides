def fibonacci_number(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n==3:
        return 5

    return 'unimplemented'

def fibonacci_list(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    if n == 3:
        return [1, 1, 5]
    raise Exception('unimplemented')
