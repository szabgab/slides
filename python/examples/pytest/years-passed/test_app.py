import app
import datetime
import pytest

def test_app(monkeypatch):
    mydt = datetime.date
    class MyDate():
        def today():
            return mydt(2021, 2, 15)
        def fromisoformat(date_str):
            return mydt.fromisoformat(date_str)

    monkeypatch.setattr(app.datetime, 'date', MyDate)

    assert app.get_years_passed_category('1990-06-02') == 'More than 30 years'
    assert app.get_years_passed_category('2000-01-01') == '20 - 30 years'
    assert app.get_years_passed_category('2011-01-01') == '10 - 20 years'
    assert app.get_years_passed_category('2016-01-01') == '5 - 10 years'
    assert app.get_years_passed_category('2020-01-01') == '1 - 5 years'
    assert app.get_years_passed_category('2021-02-14') == 'Less than 1 year'
    assert app.get_years_passed_category('2021-02-15') == 'Less than 1 year'


    with pytest.raises(Exception) as err:
        app.get_years_passed_category('2021-02-16')
    assert err.type == ValueError
    assert str(err.value) == "Could not find a years_passed_category for '2021-02-16'"
