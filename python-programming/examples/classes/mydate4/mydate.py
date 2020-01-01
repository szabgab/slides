def other_method(val):
    print(val)

class Date(object):
    def __init__(self, Year, Month, Day):
        self.year  = Year
        self.month = Month
        self.day   = Day

    def __str__(self):
        return 'Date({}, {}, {})'.format(self.year, self.month, self.day)

    @classmethod
    def from_str(class_object, date_str):
        '''Call as
           d = Date.from_str('2013-12-30')
        '''
        print(class_object)
        year, month, day = map(int, date_str.split('-'))

        other_method(43)

        if class_object.is_valid_date(year, month, day):
            return class_object(year, month, day)
        else:
            raise Exception("Invalid date")

    @staticmethod
    def is_valid_date(year, month, day):
        if 0 <= year <= 3000 and  1 <= month <= 12 and 1 <= day <= 31:
            return True
        else:
            return False

