-- turn on FOREIGN KEY checking
PRAGMA foreign_keys = ON;

CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT

);


CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    manager INTEGER,
    FOREIGN KEY(manager) REFERENCES people(id)
);

INSERT INTO people (name) VALUES ('Natalie Portman ');
INSERT INTO people (name) VALUES ('Gal Gadot');
INSERT INTO people (name) VALUES ('Cole Lawrence');
INSERT INTO people (name) VALUES ('Lior Raz');
INSERT INTO people (name) VALUES ('Erick Tryzelaar');
INSERT INTO people (name) VALUES ('Ernest Kissiedu');
SELECT * FROM people;
SELECT "-----";

INSERT INTO groups (name, manager) VALUES ('Rust London', (SELECT id FROM people WHERE name = 'Ernest Kissiedu'));
INSERT INTO groups (name, manager) VALUES ('Rust NYC', (SELECT id FROM people WHERE name = 'Cole Lawrence'));
INSERT INTO groups (name, manager) VALUES ('Rust Bay Area', (SELECT id FROM people WHERE name = 'Erick Tryzelaar'));
INSERT INTO groups (name, manager) VALUES ('Other Group', 42);
SELECT * FROM people;
SELECT "";
SELECT * FROM groups;
SELECT "-----";

DELETE FROM people WHERE name = 'Cole Lawrence';
SELECT * FROM people;
SELECT "";
SELECT * FROM groups;
SELECT "-----";


