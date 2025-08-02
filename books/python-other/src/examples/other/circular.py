import time


def create_pair():
    a = {'name' : 'Foo'}
    b = {'name' : 'Bar'}
    a['pair'] = b
    b['pair'] = a
    #print(a)


for i in range(1, 30000000):
    create_pair()

print("let's sleep now a bit")
time.sleep(20)
