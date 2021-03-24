class Thing:
     def __init__(self):
         self._name = 'This should be private'

t = Thing()
print(t._name)  # This should be private
