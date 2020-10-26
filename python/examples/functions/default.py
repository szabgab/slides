def prompt(question, retry=3):
    print(question)
    print(retry)
    #while retry > 0:
    #    inp = input('{} ({}): '.format(question, retry))
    #    if inp == 'my secret':
    #        return True
    #    retry -= 1
    #return False

prompt("Type in your password")

prompt("Type in your secret", 1)

prompt("Hello", retry = 7)

# prompt(retry = 7, "Hello")  # SyntaxError: positional argument follows keyword argument

prompt(retry = 42, question = "Is it you?")

