import pathpy as pp
from pathpy.visualisation import plot, export_html

n = pp.Network(directed=True)
n.add_edge('a', 'c')
n.add_edge('b', 'c')
n.add_edge('c', 'd')
n.add_edge('c', 'e')
print(n)

export_html(n, 'network.html')  # the documentation of plot gives you the parameters that you could import here.

