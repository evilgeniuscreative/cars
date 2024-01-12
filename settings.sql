-- settings.sql
CREATE DATABASE carsdb;
CREATE USER driver WITH PASSWORD 'drive';
GRANT ALL PRIVILEGES ON DATABASE carsdb TO driver;

