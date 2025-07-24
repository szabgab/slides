CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT
);

INSERT INTO people (username) VALUES ('foo');
INSERT INTO people (username) VALUES ('bar');
SELECT * from people;

