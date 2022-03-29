from date import test_date
import re

def fix_date4(date):
    return re.sub(r'-(\d)\b', r'-0\1', date)

test_date(fix_date4)

