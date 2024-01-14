-- settings.sql
CREATE DATABASE carsdb;
CREATE USER driver WITH PASSWORD 'drive';
-- ALTER DATABASE OWNER TO driver; add this next time
GRANT ALL PRIVILEGES ON DATABASE carsdb TO driver;

