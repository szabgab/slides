CREATE TABLE people (
    id       INTEGER PRIMARY KEY,
    fname    VARCHAR(100), 
    lname    VARCHAR(100), 
    email    VARCHAR(100) UNIQUE NOT NULL,
    pw       VARCHAR(20) NOT NULL
);

INSERT INTO people (fname, lname, email, pw)
        VALUES  ('Foo',  'Bar',   'foo@bar.com',    'secret');
INSERT INTO people (fname, lname, email, pw) 
        VALUES  ('Peti', 'Bar',   'peti@bar.com',   'real secret');
INSERT INTO people (fname, lname, email, pw) 
        VALUES  ('Moo',  'Bar',   'moo@bar.com',    'no secret');
INSERT INTO people (fname, lname, email, pw) 
        VALUES  ('Foo',  'Bar',   'bar@perl.org',   'obFoo');
INSERT INTO people (fname, lname, email, pw) 
        VALUES  ('Foo',  'Berry', 'berry@perl.org', 'yrreB');
 
CREATE TABLE accounts (
    id       INTEGER PRIMARY KEY,
    owner    INTEGER UNIQUE NOT NULL, 
    amount   INTEGER
);

INSERT INTO accounts (owner, amount) VALUES (1, 1000); 
INSERT INTO accounts (owner, amount) VALUES (2, 2000); 
INSERT INTO accounts (owner, amount) VALUES (3, 0); 


CREATE TABLE cds (
    id       INTEGER PRIMARY KEY,
    title    VARCHAR(100),
    artist   INTEGER
);

