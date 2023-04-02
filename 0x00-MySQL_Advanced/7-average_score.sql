-- Stored procedure ComputeAverageScoreForUser that computes and store the averagescore of a user.
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
DECLARE average FLOAT DEFAULT 0;
SELECT AVG(score) INTO average FROM corrections WHERE corrections.user_id = user_id;
UPDATE users SET average_score = average WHERE id = user_id;
END
//
