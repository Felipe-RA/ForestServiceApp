-- Insert test data into the 'users' table if it is empty
DO $$
BEGIN
    IF (SELECT count(*) FROM users) = 0 THEN
        INSERT INTO users (username, registered_at)
        VALUES 
            ('testuser1', CURRENT_TIMESTAMP),
            ('testuser2', CURRENT_TIMESTAMP);
    END IF;
END
$$;

-- Insert test data into the 'saved_queries' table if it is empty
DO $$
BEGIN
    IF (SELECT count(*) FROM saved_queries) = 0 THEN
        INSERT INTO saved_queries (name, query_text, username, comment, created_at)
        VALUES 
            ('Query 1', 'SELECT * FROM table1', 'testuser1', 'First test query', CURRENT_TIMESTAMP),
            ('Query 2', 'SELECT * FROM table2', 'testuser2', 'Second test query', CURRENT_TIMESTAMP);
    END IF;
END
$$;
