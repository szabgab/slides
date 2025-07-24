import app
import datetime

def test_new_year(monkeypatch):
    mydt = datetime.date
    class MyDate():
        def today():
            return mydt(2000, 1, 1)

    monkeypatch.setattr(app.datetime, 'date', MyDate)
    today = app.get_today()
    #print(today)
    assert str(today) == '2000-01-01'

def test_leap_year(monkeypatch):
    mydt = datetime.date
    class MyDate():
        def today():
            return mydt(2004, 2, 29)

    monkeypatch.setattr(app.datetime, 'date', MyDate)
    today = app.get_today()
    #print(today)
    assert str(today) == '2004-02-29'


