CREATE TABLE qa (
    question TEXT,
    answer TEXT DEFAULT 42
);

INSERT INTO qa (question, answer) VALUES ('Language?', 'SQL');
INSERT INTO qa (question, answer) VALUES ('Database?', 'SQLite');
INSERT INTO qa (question) VALUES ('Meaning of life?');
SELECT * from qa;
