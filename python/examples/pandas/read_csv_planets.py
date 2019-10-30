import pandas
planets = pandas.read_csv('planets.csv', index_col='name')
print(type(planets))  # <class 'pandas.core.frame.DataFrame'>
print(planets)

planets['dm'] = planets['distance'] * planets['mass']
print(planets.head())

big = planets[ planets['mass'] > 20 ]
print(big)

