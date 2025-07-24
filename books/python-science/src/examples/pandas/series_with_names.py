import pandas

planets       = ['Mercury', 'Venus', 'Earth', 'Mars']
distances_raw = [    0.4  ,   0.7  ,       1,  1.5  ]
masses_raw    = [    0.055,   0.815,       1,  0.107]

distance = pandas.Series(distances_raw, index = planets)
mass     = pandas.Series(masses_raw,    index = planets)

print(distance)

# Mercury     0.40
# Venus       0.70
# Earth       1.00
# Mars        1.50
# dtype: float64


print(distance.index)
# Index(['Mercury', 'Venus', 'Earth', 'Mars'], dtype='object')

print(distance[distance < 0.8])
# Mercury    0.4
# Venus      0.7
# dtype: float64


print('------')
print(distance/mass)
# Mercury         7.272727
# Venus           0.858896
# Earth           1.000000
# Mars           14.018692
# dtype: float64

