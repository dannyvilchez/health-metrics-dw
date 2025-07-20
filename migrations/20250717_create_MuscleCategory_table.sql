CREATE TABLE dw.MuscleCategory (
    MuscleCategoryID   SMALLINT       GENERATED ALWAYS AS IDENTITY  PRIMARY KEY,
    MuscleCategory     VARCHAR(10)    NOT NULL UNIQUE
);


INSERT INTO dw.MuscleCategory (MuscleCategory) VALUES 
('Abs'),
('Back'),
('Biceps'),
('Chest'),
('Forearms'),
('Legs'),
('Shoulders'),
('Triceps');
