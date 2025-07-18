CREATE TABLE test_migration (
    id               SMALLINT     GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name             TEXT         NOT NULL,
    created_date     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO test_migration (name) VALUES ('danny');
