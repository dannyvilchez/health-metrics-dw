CREATE TABLE dw.Grip (
    GripID        SMALLINT        GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    GripName      TEXT            NOT NULL UNIQUE
);



