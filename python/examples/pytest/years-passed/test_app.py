import app
import datetime

#for date in ['2000-01-01', '1990-06-02', '2020-01-01']:
def test_app(monkeypatch):
    mydt = datetime.date
    class MyDate():
        def today():
            return mydt(2021, 2, 15)
        def fromisoformat(date_str):
            return mydt.fromisoformat(date_str)

    monkeypatch.setattr(app.datetime, 'date', MyDate)

    date = '2000-01-01'
    cat = '20 - 30 years'

    category = app.get_years_passed_category(date)
    assert cat == category

