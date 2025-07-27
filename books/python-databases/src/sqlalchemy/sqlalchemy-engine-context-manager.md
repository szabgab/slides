# SQLAlchemy engine using context managers


```
with engine.begin() as trans:
    conn.execute(...)
    conn.execute(...)
    raise Exception()  # for rollback
```


