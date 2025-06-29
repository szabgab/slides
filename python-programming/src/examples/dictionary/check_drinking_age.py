
limit = {
    'Japan': 20,
    'USA': 21,
    'Ethiopia': 15,
}

filename = 'alcohol_in.csv'
with open(filename) as fh:
    for line in fh:
        line = line.rstrip('\n')
        country, agestr = line.split(',')
        age = float(agestr)
        if country in limit:
            if limit[country] < age:
                print("yes"
