-- Filename: backend/sql/01_create_users_table.sql

-- This script creates a table for storing user information.

CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255) PRIMARY KEY,         -- A unique username for each user
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- The timestamp when the user first registered a query
);
