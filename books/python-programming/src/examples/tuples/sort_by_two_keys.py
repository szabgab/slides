
planets1 = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
planets2 = ['Mercury', 'Earth', 'Venus', 'Mars', 'Jupiter', 'Saturn']

print(sorted(planets1, key=len))
# ['Mars', 'Venus', 'Earth', 'Saturn', 'Mercury', 'Jupiter']
print(sorted(planets2, key=len))
# ['Mars', 'Earth', 'Venus', 'Saturn', 'Mercury', 'Jupiter']

print(sorted(planets1, key=lambda w: (len(w), w)))
# ['Mars', 'Earth', 'Venus', 'Saturn', 'Jupiter', 'Mercury']
print(sorted(planets2, key=lambda w: (len(w), w)))
# ['Mars', 'Earth', 'Venus', 'Saturn', 'Jupiter', 'Mercury']
