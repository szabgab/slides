names = ['Jan', 'Feb', 'Mar', 'Apr']
days =  [31, 28, 31, 30]

month = dict(zip(names, days))
print(month)   # {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30}


zipper = zip(names, days)
print(zipper)        # <zip object at 0x7ff7c7d0db48>
print(list(zipper))  # [('Jan', 31), ('Feb', 28), ('Mar', 31), ('Apr', 30)]

