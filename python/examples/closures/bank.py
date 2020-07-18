def create_bank(n = 0):
    balance = n
    def bnk(change = 0, prev=False):
        nonlocal balance
        prev_balance = balance
        balance += change
        if prev:
            return prev_balance
        else:
            return balance
    return bnk


bank = create_bank(20)

print(bank())    # 20
print(bank(7))   # 27
print(bank())    # 27
print(bank(-3))  # 24
print(bank())    # 24


print(bank(10, prev=True))   # 24
print(bank())    # 34

