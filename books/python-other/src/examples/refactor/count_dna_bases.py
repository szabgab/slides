import sys
import os

def getinput():
    string = []
    if len(sys.argv)<2:
        exit(f'USE: {sys.argv[0]} FILE'.center(40,' -'))
    elif os.path.isfile(sys.argv[1]):
        file = sys.argv[1]
    else:
        file = 0

    if file:
        with open(file) as f:
            for line in f:
                string.append(line.strip('\n'))

        try:
            string = ''.join(string)
        except Exception:
            exit('EXCEPTION IN INPUT'.center(40,' -'))
    else:
        string = sys.argv[1]

    return(string)


#def funique(items):
#    unique = []
#
#    filt = [' ', '.', ',', ':']
#    items = list(filter(lambda x : x not in filt ,items))
#
#    for item in items:
#        if item.split()[0] not in unique:
#            unique.append(item.split()[0])
#    return(unique)

# def count(unique,items):
#
#     count = [0]*len(unique)
#     print(count)
#     diction = {unique[i]:count[i] for i in range(len(unique))}
#     print(type(diction))
#     for u in unique:
#         print('from count unique: ',u)
#         for item in items:
#             print('from count item: ',item)
#             if u == item:
#                 print(True)
#                 print(type(u))
#                 print(diction['A'],diction['T'])
#                 diction[u][0] += 1
#                 print(id(diction['A']),id(diction['T']))
#                 print(diction)
#                 return
#     return(diction)

# In[162]:


def count(items):

    filt = [' ', '.', ',', ':']
    items = list(filter(lambda x : x not in filt ,items))

    diction = {}
    for item in items:
        if item in diction.keys():
            diction[item] += 1
        else:
            diction[item] = 1
    return(diction)


def out(diction):
    sort = sorted(d)
    summ = sum(diction[x] for x in diction.keys())
    for key in sort:
        percent = (d[key]/summ)*100
        print(f'{key:<2}{d[key]:<3}-{percent:>6.2f} %')


items = getinput()
d = count(items)
out(d)

