import sys
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '1')
# print(path)  # /home/gabor/work/slides/python-programming/examples/package/1
sys.path.insert(0, path)

import mymath.calc
print(mymath.calc.add(2, 5))

from mymath.calc import add
print(add(2, 3))
