-- Add one bonus of an existing project
SELECT * FROM users;
SELECT * FROM projects;
SELECT * FROM corrections;

SELECT "--";

CALL AddBonus((SELECT id FROM users WHERE name = "user_1"), "project_2", 98);

SELECT "--";

SELECT * FROM users;
SELECT * FROM projects;
SELECT * FROM corrections;
