CREATE TABLE people (
    name TEXT,
    grade INTEGER
);

INSERT INTO people (name, grade) VALUES ('Joe', 40);
INSERT INTO people (name, grade) VALUES ('Jane', 60);
SELECT * from people;
SELECT "";

UPDATE people SET grade = 44 WHERE name = "Joe";
SELECT * from people;
SELECT "";

UPDATE people SET grade = (SELECT grade FROM people WHERE name = "Joe") + 1 WHERE name = "Joe";
SELECT * from people;
SELECT "";

