import sys
import pandas as pd

filename = "planets.csv"
center = 'Earth'
if len(sys.argv) > 1:
    center   = sys.argv[1]
if len(sys.argv) > 2:
    filename = sys.argv[2]

df = pd.read_csv(filename)

this = df[ df['Planet name'] == center ]
print(this)
print('----')

mass = this.iloc[0]['Mass']
print(mass)
print('----')

dist = this.iloc[0]['Distance (AU)']
print(dist)
print('----')


# gravitational force is F = G * (mass1*mass2) / distance**2
G = 6
distance = abs(dist - df['Distance (AU)'])
print(distance)
print('----')

forces = df.copy()
print(forces)
print('----')


F = G * (df['Mass'] * mass) / distance**2
print(F)
print('----')

forces['F'] = F
forces.drop(columns = 'Mass', inplace=True)
forces.drop(columns = 'Distance (AU)', inplace=True)
print(forces)
print('----')

