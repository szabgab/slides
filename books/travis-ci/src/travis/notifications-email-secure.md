# notifications email secure - sending to multiple addresses



```
travis encrypt "joe@example.com" --add notifications.email.recipients
```


This will want to rewrite and reformat yout `.travis.yml`. If you are ok with it then let it do it.
If you don't want it to change your config file, then instead of that you might copy the new section it offers to add to
your file and then you can add it manually. It will look something like this:


```
notifications:
  email:
    recipients:
      secure: c6AsRDQshSjrw+JIlaH7XbusT2zqVMAdhbFTWFogKc4LY9ytK2K2i2FVYp015p/14SRSK8HBYOpXJ3uy+vGBS2Eyovq0WSnTki7MLpx1GXhPOUyuiiLhtgHiTRzTK/3BdTlIOc9uKnw7Urw=
```

* Add another email address:

```
travis encrypt "jane@example.com" --append --add notifications.email.recipients
```

The result will look like this:

```
notifications:
  email:
    recipients:
      - secure: c6AsRDQshSjrw+JIlaH7XbusT2zqVMAdhbFTWFogKc4LY9ytK2K2i2FVYp015p/14SRSK8HBYOpXJ3uy+vGBS2Eyovq0WSnTki7MLpx1GXhPOUyuiiLhtgHiTRzTK/3BdTlIOc9uKnw7Urw=
      - secure: AsAAlsjfkshkSADQshSjrw+JIlaH7XbusT2zqVMAdhbFTWFogKc4LY9ytK2K2i2FVYp015p/14SRSK8HBYOpXJ3uy+vGBS2Eyovq0WSnTki7MLpx1GXhPOUyuiiLhtgHiTRzTK/3BdTlSFF=
```


It seems this will work without the "recipients" key as well but then only with one email address, even if you supply two.



