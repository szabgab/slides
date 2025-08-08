# crontab

* crontab

```
$ crontab -e       (edit)
*  *  *  *  * date >> ~/out.txt
```

```
man 5 crontab
```

```
crontab -l         (list)
```


User specific file:


```
/var/spool/cron/crontabs/USERNAME
```

System-wide crontab files:


```
/etc/cron.d/
/etc/cron.daily/
/etc/cron.hourly/
/etc/cron.monthly/
/etc/crontab
/etc/cron.weekly/
```


