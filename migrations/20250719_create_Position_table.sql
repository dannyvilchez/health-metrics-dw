CREATE TABLE dw.Position (
    PositionID        SMALLINT        GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    PositionName      TEXT            NOT NULL UNIQUE
);

INSERT INTO dw.Position (PositionName)
VALUES 
    ('None'),
    ('Seated'),
    ('Standing'),
    ('Incline'),
    ('Flat');

