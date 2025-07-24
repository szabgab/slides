CREATE TABLE qa (
    question TEXT,
    answer INTEGER
);

INSERT INTO qa (question, answer) VALUES ('2+2', 4);
INSERT INTO qa (question, answer) VALUES ('2-2', 0);
INSERT INTO qa (question) VALUES ('Meaning of life?');
SELECT * from qa;

