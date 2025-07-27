CREATE TABLE node (
    id      INTEGER PRIMARY KEY,
    name    VARCHAR(100)
);

CREATE TABLE interface (
    id       INTEGER PRIMARY KEY,
    node_id  INTEGER NOT NULL,
    ipv4     VARCHAR(15) UNIQUE,
    ipv6     VARCHAR(80) UNIQUE,
    FOREIGN KEY (node_id) REFERENCES node(id)
);

CREATE TABLE connection (
    a        INTEGER NOT NULL,
    b        INTEGER NOT NULL,
    FOREIGN KEY (a) REFERENCES interface(id),
    FOREIGN KEY (b) REFERENCES interface(id)
);
