
def run_these(value, *functions):
    print(functions)
    for func in functions:
        print(func(value))

run_these("abc", len, lambda x: x+x,  lambda y: f"text: {y}")
