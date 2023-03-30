-- Create a trigger to automattically decrement the items table by number of orders

CREATE TRIGGER items_ref BEFORE INSERT ON orders
FOR EACH ROW
	UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
