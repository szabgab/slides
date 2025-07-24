names = ["Helen", "Ann", "Mary", "Harry", "Joe", "Peter"]
names3 = filter(lambda w: len(w) == 3, names)
print( list(names3) )

loc3 = filter(lambda i: len(names[i]) == 3, range(len(names)))
print( list(loc3) )


has_e = filter(lambda i: "e" in names[i], range(len(names)))

print( list(has_e) )

