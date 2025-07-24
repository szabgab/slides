
def div(a, b):
    try:
        print("try")
        c = a / b
    except Exception:
        print("exception")
        return
    finally:
        print("finally")

div(2, 1)
print('---')
div(2, 0)

