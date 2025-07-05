# Health Metrics Data Warehouse

This is a postgres data warehouse that stores all of my health and fitness data. It will serve as the main data store for my future svelte data stories.

##  Phase 1: Health & Fitness Data Warehouse

**Goal:** Centralize and model your raw health and fitness data from multiple sources in a local PostgreSQL data warehouse.

###  Completed Milestones

1. **Local PostgreSQL Setup**
   - `docker-compose` used to spin up a containerized `postgres` database.
   - `.env` file stores database credentials.

2. **Schema Migration Tool: `migrate.py`**
   - Python script to apply SQL migration files to the database.
   - Tracks applied migrations via a `schema_migrations` table.
   - Skips any already-applied `.sql` files to support idempotent runs.


### Local Development Setup

1. Clone the repo.
2. Create a .env file in the root directory
    - PG_HOST=localhost
    - PG_PORT=5432
    - PG_NAME=your_database
    - PG_USER=your_user
    - PG_PASSWORD=your_password
3. Run postgres locally: `docker-compose up -d`
⸻

#### Running Migrations
	1. Place SQL migration files in the migrations/ directory. File naming convention: YYYYMMDD_filename.sql
	2. Run the migration script: python3 migrations/migrate.py

This will:
	• Connect to the database using .env
	• Create the schema_migrations table (if it doesn’t exist)
	• Apply any new .sql files not yet recorded

