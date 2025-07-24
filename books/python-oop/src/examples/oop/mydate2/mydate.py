class Date:
    def __init__(self, Year, Month, Day):
        self.year  = Year
        self.month = Month
        self.day   = Day

    def __str__(self):
        return 'Date({}, {}, {})'.format(self.year, self.month, self.day)

    def set_date(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    @classmethod
    def from_str(cls, date_str):
        '''Call as
           d = Date.from_str('2013-12-30')
        '''
        print(cls)
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)

