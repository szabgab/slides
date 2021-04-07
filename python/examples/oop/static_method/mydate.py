class Date(object):
    def __init__(self, Year, Month, Day):
        if not Date.is_valid_date(Year, Month, Day):
            raise Exception('Invalid date')
        self.year  = Year
        self.month = Month
        self.day   = Day

    def __str__(self):
        return 'Date({}, {}, {})'.format(self.year, self.month, self.day)

    @staticmethod
    def is_valid_date(year, month, day):
        if 0 <= year <= 3000 and  1 <= month <= 12 and 1 <= day <= 31:
            return True
        else:
            return False


