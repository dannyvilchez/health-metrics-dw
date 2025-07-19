CREATE TABLE dw.Equipment (
    EquipmentID        SMALLINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    EquipmentName      TEXT     NOT NULL UNIQUE
);


INSERT INTO dw.Equipment (EquipmentName)
VALUES 
    ('Bodyweight'),
    ('Machine'),
    ('None'),
    ('Cable'),
    ('Dumbbell'),
    ('EZ Bar'),
    ('Barbell'),
    ('Parallettes');
