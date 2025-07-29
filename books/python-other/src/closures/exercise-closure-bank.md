# Exercise: closure bank

* Create a closure that returns a function that holds a number (like a bank account) that can be incremented or decremented as follows:
* Allow for an extra paramter called `prev` that defaults to `False`. If `True` is passed then instead of returning the new balance, return the old balance.

```
bank = create_bank(20)

print(bank())    # 20
print(bank(7))   # 27
print(bank())    # 27
print(bank(-3))  # 24
print(bank())    # 24


print(bank(10, prev=True))   # 24
print(bank())    # 34
```



