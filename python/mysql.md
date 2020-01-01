# MySQL
{id: mysql}

## Install MySQL support
{id: install-mysql-support}

* Anaconda on MS Windows: **conda install mysql-connector-python**
* Otherwise: **pip install mysql-connector**



## Create database user (manually)
{id: create-database-user}

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


## Create database (manually)
{id: create-database}

```
$ mysql -u foobar -p 

  CREATE DATABASE fb_db;

  DROP DATABASE fb_db;
  exit
```


## Create table (manually)
{id: create-table}

```
$ mysql -u foobar -p 

  USE fb_db;
  CREATE TABLE person (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    birthdate DATE,
    score REAL
  );

  INSERT INTO person (name, birthdate, score)
      VALUES ("Foo Bar", "1998-05-23", 42.1)
```


## Connect to MySQL
{id: connect-to-mysql}
{i: connect}
{i: close}
![](examples/mysql/connect.py)

```
$ python3 examples/mysql/connect.py
```

* Change some of the parameters and try again



## Connect to MySQL and Handle exception
{id: connect-to-mysql-handle-exception}
![](examples/mysql/connect_exception.py)


## Select data
{id: select-data}
{i: cursor}
{i: execute}
{i: fetchone}
![](examples/mysql/select_data.py)


## Select more data
{id: select-more-data}
![](examples/mysql/select_more_data.py)


## Select all data fetchall
{id: select-all-data}
{i: fetchall}
![](examples/mysql/select_all_data.py)



## Select some data fetchmany
{id: select-some-data}
{i: fetchmany}
![](examples/mysql/select_some_data.py)


## Select some data WHERE clause
{id: selected-data}
{i: WHERE}
{i: %s}

[Bobby Tables](http://bobby-tables.com/)

![](examples/mysql/selected_data.py)


## Select into dictionaries
{id: select-dictionary}
![](examples/mysql/select_dicts.py)



## Insert data
{id: insert-data}
{i: INSERT}
{i: commit}
![](examples/mysql/insert_data.py)


## Update data
{id: update-data}
{i: UPDATE}
![](examples/mysql/update_data.py)


## Delete data
{id: delete-data}
{i: DELETE}
![](examples/mysql/delete_data.py)


## Exercise MySQL
{id: exercise-mysql}

1. Create a user with a password manually.
1. Create a database manually.
1. Create a table manually for describing fleet of cars: id, license-plate, year-built, brand, owner. (Owner is the name of the owner)
1. Create a program that accepts values on the command line and insterts the data in the database
1. Create another program that lists all the cars.
1. Improve the selector program to accept command line paramter --minage N and --maxage N and show the cars within those age limits (N is a number of years e.g. 3)
1. Create program to delete a car.
1. Create program to change the owner of a car.



## Exercise: MySQL Connection
{id: exercise-mysql-connection}

Instead of hard-coding the connection details in the script, let's create an INI file that contains the connection information and use that.


![](examples/mysql/connect.ini)


## Solution: MySQL Connection
{id: solution-mysql-connection}
![](examples/mysql/connect_config.py)





