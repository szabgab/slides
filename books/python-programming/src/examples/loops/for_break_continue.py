txt = 'hello world'
for cr in txt:
    if cr == ' ':
        continue
    if cr == 'r':
        break
    print(cr)

print('done')
