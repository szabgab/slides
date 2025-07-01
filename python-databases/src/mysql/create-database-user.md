# Create database user (manually)


```
$ mysql -u root -p 

   SHOW DATABASES;

   CREATE USER 'foobar'@'localhost' IDENTIFIED BY 'no secret';
   GRANT ALL PRIVILEGES ON fb_db . * TO 'foobar'@'localhost';
   GRANT ALL PRIVILEGES ON * . * TO 'foobar'@'%' IDENTIFIED BY 'no secret';
   FLUSH PRIVILEGES;

   exit
```


```
   vim /etc/mysql/mysql.conf.d/mysqld.cnf
   comment out
   # bind-address          = 127.0.0.1
 
   service mysql restart
```


