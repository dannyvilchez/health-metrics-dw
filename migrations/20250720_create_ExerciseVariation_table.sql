CREATE TABLE dw.ExerciseVariant (
    VariantID        SMALLINT        GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ExerciseID       SMALLINT        NOT NULL REFERENCES dw.Exercise(ExerciseID),
    EquipmentID      SMALLINT        NOT NULL REFERENCES dw.Equipment(EquipmentID),
    PositionID       SMALLINT        NOT NULL REFERENCES dw.Position(PositionID),
    GripID           SMALLINT        NOT NULL REFERENCES dw.Grip(GripID),
    IsAssisted       BOOLEAN         NOT NULL DEFAULT false,
    VariantName      TEXT            NOT NULL UNIQUE
);
