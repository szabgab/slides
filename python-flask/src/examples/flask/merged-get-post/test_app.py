import app
import pytest


def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<a href="/calc">calc</a>' == rv.data


def test_calc():
    web = app.app.test_client()

    rv = web.get('/calc')
    assert rv.status == '200 OK'
    assert b'<form' in rv.data

    rv = web.post('/calc', data={'a': 7, 'b': 11})
    assert rv.status == '200 OK'
    assert b'18.0' == rv.data
