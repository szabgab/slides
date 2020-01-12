import sys
import os

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    '1' ) )

import mymath.calc
print(mymath.calc.add(2, 5))  # 7

from mymath.calc import add
print(add(2, 3))              # 5
