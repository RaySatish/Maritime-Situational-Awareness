-- Create the database
CREATE DATABASE maritime_data;

-- Connect to the database
\c maritime_data

-- Enable the PostGIS extension
CREATE EXTENSION postgis;

-- Create table to store maritime contacts
CREATE TABLE maritime_contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    issue TEXT,
    geom GEOMETRY(Point, 4326),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
