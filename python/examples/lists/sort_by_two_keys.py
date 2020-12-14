
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']

print(sorted(planets, key=len))
# ['Mars', 'Venus', 'Earth', 'Saturn', 'Mercury', 'Jupiter']


print(sorted(planets, key=lambda w: (len(w), w)))
# ['Mars', 'Earth', 'Venus', 'Saturn', 'Jupiter', 'Mercury']
