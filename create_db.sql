CREATE ROLE spa_cti WITH LOGIN PASSWORD 'spa_cti'  CREATEDB;

CREATE DATABASE spa_cti_dev;

GRANT ALL PRIVILEGES ON DATABASE "spa_cti_dev" to spa_cti;