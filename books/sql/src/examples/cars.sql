CREATE TABLE car (
    owner_name    VARCHAR(100),
    color         VARCHAR(20) NOT NULL,
    license_plate VARCHAR(20) UNIQUE,
    motor_number  VARCHAR(20) UNIQUE NOT NULL
);
