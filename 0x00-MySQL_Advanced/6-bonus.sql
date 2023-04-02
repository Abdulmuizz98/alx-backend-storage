-- Stored procedure AddBonus that adds a new correction for a student.
DELIMITER //
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
DECLARE pid INT DEFAULT 0;
SELECT id INTO pid FROM projects WHERE projects.name = project_name;
IF pid = 0
THEN
INSERT INTO projects (name) VALUES (project_name);
SET pid = LAST_INSERT_ID();
END IF;
INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, pid, score);
END
//
