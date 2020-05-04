CREATE TABLE friends (
    id INTEGER,
    name_ TEXT,
    birthday DATE

);

INSERT INTO friends (id, name, birthday)
VALUES (1, 'Jane Doe', '1990-05-30');

INSERT INTO friends (id, name, birthday)
VALUES (2, 'BFF One', '1990-01-01');

INSERT INTO friends (id, name, birthday)
VALUES (3, 'BFF Two', '1990-02-02');

UPDATE friends
SET name = 'Jane Smith'
WHERE id = 1;

SELECT * FROM friends;