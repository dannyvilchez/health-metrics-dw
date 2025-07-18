CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS dw;


CREATE TABLE dw.WeightUnit (
    WeightUnitID       SMALLINT     GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    WeightUnit         VARCHAR(3)   NOT NULL
);


INSERT INTO dw.WeightUnit (WeightUnit) 
VALUES 
    ('lbs'),
    ('kg');
