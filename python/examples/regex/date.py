import re

def test_date(function):
    dates = {
        '2010-7-5'   : '2010-07-05',
        '2010-11-5'  : '2010-11-05',
        '2010-07-5'  : '2010-07-05',
        '2010-07-05' : '2010-07-05',
        '2010-7-15'  : '2010-07-15',
    }

    failures = 0
    for original in sorted(dates.keys()):
        result = function(original)

        if result != dates[original]:
            failures += 1
            print(f"      old: {original}")
            print(f"      new: {result}")
            print(f" expected: {dates[original]}")
            print("")
    if failures == 0:
        print("Everything looks good")
    else:
        exit(failures)

