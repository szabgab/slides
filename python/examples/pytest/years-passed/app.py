import datetime
import math

def get_years_passed_category(date_string):
    date = datetime.date.fromisoformat(date_string)
    time_passed = datetime.date.today() - date
    years_passed = time_passed.days // 365
    years_passed_start_and_end_range_tuples_to_category = {
        (0, 1):    "Less than 1 year",
        (1, 5):    "1 - 5 years",
        (5, 10):   "5 - 10 years",
        (10, 20):  "10 - 20 years",
        (20, 30):  "20 - 30 years",
        (30, math.inf): "More than 30 years"
    }
    for (start, end), category in years_passed_start_and_end_range_tuples_to_category.items():
        if start <= years_passed < end:
            return category

    raise ValueError(f"Could not find a years_passed_category for '{date_string}'")
