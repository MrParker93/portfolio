-- Check if the table exists
DROP TABLE IF EXISTS email;

-- Create a table to store emails received
CREATE TABLE email(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email VARCHAR(255),
    subject TEXT NOT NULL,
    message TEXT NOT NULL
);