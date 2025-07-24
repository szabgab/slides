CREATE TABLE person (
    name       VARCHAR(100),
    height     FLOAT,         -- in meter
    weight     INTEGER,       -- in kg
    birthday   DATE,
    occupation VARCHAR(100),
    gender     ENUM('male', 'female')
);

