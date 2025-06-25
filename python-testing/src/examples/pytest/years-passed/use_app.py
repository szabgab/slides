import app

for date in ['2000-01-01', '1990-06-02', '2020-01-01']:
    cat = app.get_years_passed_category(date)
    print(f"{date} : {cat}")

