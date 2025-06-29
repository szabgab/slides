def func(**kw):
    print(kw)

func(a = 23,
    b = 19,)

z = {
    'c': 10,
    'd': 20,
}

func(z = z)

func(**z)
