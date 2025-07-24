from collections import defaultdict

x = defaultdict(list)
x["b"].append("vv")
print(x)
print('---')
for z in x.keys():
    print(z)
