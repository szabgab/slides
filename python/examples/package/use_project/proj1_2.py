import sys
import os

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    '1' ) )

import mymath
print(mymath.calc.add(4, 7))
