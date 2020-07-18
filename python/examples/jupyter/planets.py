%config IPCompleter.greedy=True
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


planets = pd.read_csv('planets.csv')
planets

planets.__class__.__name__
planets.columns
planets.dtypes
planets.index
planets.values
planets.describe()

#planets.sort_values('Mass', ascending=False)
planets.sort_values('Planet name', ascending=False)

planets.Mass
planets['Planet name']
planets[2:5]
planets.loc[3:6, ['Mass', 'Planet name']]
planets.Mass > 1

planets[planets.Mass > 1]
planets['Planet name'].isin(['Earth', 'Mars'])
planets[ planets['Planet name'].isin(['Earth', 'Mars']) ]

planets[(planets.Mass > 1) &amp; (planets.Mass < 100)]
# element-wise boolean and

center = 'Earth'
this = planets[ planets['Planet name'] == center ]
mass = this.iloc[0]['Mass']
dist = this.iloc[0]['Distance (AU)']

# gravitational force is F = G * (mass1*mass2) / D**2
G = 6
D = abs(dist - planets['Distance (AU)'])
D

forces = planets.copy()
forces

G * (planets.Mass * mass) / D**2
forces['F'] = G * (planets.Mass * mass) / D**2
forces.drop(columns = 'Mass', inplace=True)
forces.drop(columns = 'Distance (AU)', inplace=True)
forces

