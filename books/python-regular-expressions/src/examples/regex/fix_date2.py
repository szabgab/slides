from date import test_date
import re

def fix_date2(date):
    return re.sub(r'-(\d)-', r'-0\1', date)

test_date(fix_date2)

