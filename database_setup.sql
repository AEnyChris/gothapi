-- change username and password as required
CREATE DATABASE gothapi;
CREATE USER aenychris WITH PASSWORD '***********';
ALTER ROLE aenychris SET client_encoding TO 'utf8';
ALTER ROLE aenychris SET default_transaction_isolation TO 'read committed';
ALTER ROLE aenychris SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE gothapi TO aenychris;