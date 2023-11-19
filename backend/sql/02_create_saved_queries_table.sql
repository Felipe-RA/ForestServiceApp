-- Filename: backend/sql/02_create_saved_queries_table.sql

-- This script creates a table for storing saved queries with a reference to the users table.

CREATE TABLE IF NOT EXISTS saved_queries (
    id SERIAL PRIMARY KEY,                     -- A unique ID for each saved query
    name VARCHAR(255) NOT NULL,                -- The name given to the saved query
    query_text TEXT NOT NULL,                  -- The actual query text
    username VARCHAR(255) NOT NULL REFERENCES users(username), -- Foreign key reference to the users table
    comment TEXT,                              -- An optional comment about the query
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- The timestamp when the query was saved
);
