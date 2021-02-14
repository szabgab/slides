import app
import datetime

def test_new_year(monkeypatch):
    mydt = datetime.datetime
    class MyDatetime():
        def now():
            return mydt(2000, 1, 1)

    monkeypatch.setattr(app.datetime, 'datetime', MyDatetime)
    task_name = app.daily_task()
    print(task_name)
    assert task_name == 'new_year'


def test_leap_year(monkeypatch):
    mydt = datetime.datetime
    class MyDatetime():
        def now():
            return mydt(2004, 2, 29)

    monkeypatch.setattr(app.datetime, 'datetime', MyDatetime)
    task_name = app.daily_task()
    print(task_name)
    assert task_name == 'leap_day'


def test_today():
    task_name = app.daily_task()
    print(task_name)
    assert task_name == 'regular'

