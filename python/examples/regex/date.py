import re

def fix_date(date):
    return re.sub(r'-(\d)\b', r'-0\1', date)


dates = {
    '2010-7-5'   : '2010-07-05',
    '2010-07-5'  : '2010-07-05',
    '2010-07-05' : '2010-07-05',
    '2010-7-15'  : '2010-07-15',
}

for original in sorted(dates.keys()):
    result = fix_date(original)

    assert result == dates[original]

    print(f"      old: {original}")
    print(f"      new: {result}")
    print(f" expected: {dates[original]}")
    print("")

