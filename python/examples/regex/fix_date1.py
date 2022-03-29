from date import test_date
import re

def fix_date1(date):
    return re.sub(r'-(\d)', r'-0\1', date)

test_date(fix_date1)

