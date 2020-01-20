# Scheduling processes
{id: schedule-process}

## crontab
{id: cron}
{i: crontab}

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


## Load crontab file
{id: load-crontab-file}

```
$ crontab ~/cron.txt
```


## crontab examples
{id: crontab-examples}
![](examples/crontab.txt)


## Schedule using at or batch
{id: at}
{i: at}
{i: atq}
{i: atrm}

* at - Schedule a job at a specific time.
* batch - execute when system load is low.





