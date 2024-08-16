UPDATE bank SET balance = (SELECT balance FROM bank WHERE name = "Mary") - 100 WHERE name = "Mary";
UPDATE bank SET balance = (SELECT balance FROM bank WHERE name = "Jane") + 100 WHERE name = "Jane";

