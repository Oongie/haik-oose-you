/* Initialise database to store users and posts */
DROP TABLE IF EXISTS fact_poem;

CREATE TABLE fact_poem (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    poem TEXT NOT NULL, -- The poem submitted for checking,
    request_tstamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP --The time the poem was submitted
);