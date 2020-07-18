things = set(['table', 'chair', 'door', 'chair', 'chair'])
print(things)
print(things.__class__)
print(things.__class__.__name__)

if 'table' in things:
   print("has table")

