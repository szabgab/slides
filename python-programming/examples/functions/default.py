def prompt(question, retry=3):
    while retry > 0:
        inp = raw_input('{} ({}): '.format(question, retry))
        if inp == 'my secret':
            return True
        retry -= 1
    return False

print(prompt("Type in your password"))

print(prompt("Type in your secret", 1))

