-- Create an index on the username column in saved_queries (useful when looking for queries by username)
CREATE INDEX idx_saved_queries_username ON saved_queries(username);
