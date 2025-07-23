DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'admin') THEN
      CREATE ROLE admin WITH LOGIN PASSWORD 'password';
   END IF;

   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'FIT') THEN
      CREATE DATABASE "FIT" OWNER admin;
   END IF;
END
$$
