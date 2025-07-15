# 3NF Core Data Model

This layer represents the normalized core of the data warehouse, modeled in 3rd Normal Form (3NF). It serves as the authoritative source for clean, structured weightlifting and training data. All downstream analytics and dimensional models will be derived from this layer.

---

## Tables and Descriptions

- **Exercise**: Stores individual strength training movements, including variations (e.g., "Pull-Up (Neutral Grip)").
- **MuscleCategory**: Defines broad muscle groups (e.g., Chest, Back, Legs) for high-level grouping.
- **Muscle**: Lists specific muscles (e.g., Lats, Biceps Short Head), each linked to a `MuscleCategory`.
- **ExerciseMuscle**: Many-to-many mapping between `Exercise` and `Muscle`, with an `IsPrimary` flag to indicate the main target muscle.
- **Activity**: Represents a complete workout session, such as a strength workout or run, tied to a date and activity type.
- **ActivityType**: Lookup table that defines types of training activities (e.g., Strength, Running, Swimming).
- **StrengthSet**: Logs a single set of an exercise within a strength-focused `Activity`, including exercise, reps, weight, and units.
- **Mesocycle**: Represents a structured training block (e.g., hypertrophy or deload phases), linked to a start and end date.
- **WeightUnit**: Defines the unit of weight used in tracking (e.g., kg, lbs).
- **Calendar**: Standard date dimension used for joining and aggregating time-based data across the warehouse.

---

## Notes

- `Activity` is the container for a full workout; multiple `StrengthSet` rows may be linked to one `Activity`.
- Each `Exercise` can target multiple muscles via `ExerciseMuscle`, supporting detailed training analysis.
