CREATE TABLE dw.Exercise (
    ExerciseID        SMALLINT        GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Exercise          VARCHAR(30)     NOT NULL
);


INSERT INTO dw.Exercise (Exercise) 
VALUES 
    ('Back Extension'),
    ('Bench Press'),
    ('Bicep Curl'),
    ('Calf Extension'),
    ('Chest Dip'),
    ('Chest Fly'),
    ('Face Pull'),
    ('Forearm Curl'),
    ('Glute Bridge'),
    ('Hanging Leg Raise'),
    ('Hip Abductor'),
    ('Hip Adductor'),
    ('Lat Pulldown'),
    ('Lateral Raise'),
    ('Leg Curl'),
    ('Leg Extension'),
    ('Leg Press'),
    ('Lunge'),
    ('Shoulder Press'),
    ('Overhead Tricep Extension'),
    ('Pull Up'),
    ('Push Up'),
    ('Romanian Dead Lift'),
    ('Rear Delt Fly'),
    ('Seated Row'),
    ('Shrug'),
    ('Skullcrushers'),
    ('Squat'),
    ('Tricep Pushdown'),
    ('Triceps Dip');
