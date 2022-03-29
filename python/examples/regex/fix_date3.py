from date import test_date
import re

def fix_date3(date):
    return re.sub(r'-(\d)(-|$)', r'-0\1\2', date)

test_date(fix_date3)

