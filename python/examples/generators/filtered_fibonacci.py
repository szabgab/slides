from series import fibonacci

even = ( f for f in fibonacci() if f % 2 == 0 )
for e in even:
    print(e)
    if e > 40:
        break
