-- Create a trigger to automattically decrement the items table by number of orders

DELIMITER //
CREATE TRIGGER valid_ref BEFORE UPDATE ON users
FOR EACH ROW
	BEGIN
	IF NEW.email <> OLD.EMAIL THEN
	SET NEW.valid_email = 0;
	END IF;
	END
	//
