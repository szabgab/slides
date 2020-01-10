class Date(object):
    total = 0

    def __init__(self, Year, Month, Day):
        self.year  = Year
        self.month = Month
        self.day   = Day
        Date.total += 1

    def __str__(self):
        return 'Date({}, {}, {})'.format(self.year, self.month, self.day)

    def set_date(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    @classmethod
    def get_total(cls):
        print(cls)
        return cls.total
