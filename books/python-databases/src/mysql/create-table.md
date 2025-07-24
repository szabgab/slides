# Create table (manually)


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


