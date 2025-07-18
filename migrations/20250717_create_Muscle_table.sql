CREATE TABLE dw.Muscle (
    MuscleID            SMALLINT        GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    MuscleCategoryID    SMALLINT        REFERENCES dw.MuscleCategory (MuscleCategoryID), 
    Muscle              VARCHAR(20)     NOT NULL
);


INSERT INTO dw.Muscle (MuscleCategoryID, Muscle) 
SELECT
    mc.MuscleCategoryID,
    m.Muscle
FROM (
    VALUES
    ('Abs', 'Lower Abs'),
    ('Abs', 'Obliques'),
    ('Abs', 'Upper Abs'),
    ('Back', 'Lats'),
    ('Back', 'Lower Back'),
    ('Back', 'Mid Back'),
    ('Back', 'Upper Back'),
    ('Biceps', 'Brachialis'),
    ('Biceps', 'Long Head'),
    ('Biceps', 'Short Head'),
    ('Chest', 'Lower Chest'),
    ('Chest', 'Mid Chest'),
    ('Chest', 'Upper Chest'),
    ('Forearms', 'Extensors'),
    ('Forearms', 'Flexors'),
    ('Legs', 'Abductors'),
    ('Legs', 'Adductors'),
    ('Legs', 'Calves'),
    ('Legs', 'Glutes'),
    ('Legs', 'Hamstrings'),
    ('Legs', 'Quads'),
    ('Shoulders', 'Front Delts'),
    ('Shoulders', 'Rear Delts'),
    ('Shoulders', 'Side Delts'),
    ('Triceps', 'Lateral Head'),
    ('Triceps', 'Long Head'),
    ('Triceps', 'Medial Head')
) AS m(MuscleCategory, Muscle)
JOIN dw.MuscleCategory mc 
  ON mc.MuscleCategory = m.MuscleCategory
